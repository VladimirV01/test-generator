import random
import sys
from datetime import datetime, timedelta

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox

import main_window

import test_dlg
import question_parser
import results


class ResultWindow(QDialog, results.Ui_Dialog):
    def __init__(self):
        super(ResultWindow, self).__init__()
        self.setupUi(self)

        self.choice = 'Cancel'
        self.ok_btn.clicked.connect(self.ok_clicked)
        self.cancel_btn.clicked.connect(self.cancel_clicked)

    def ok_clicked(self):
        self.choice = 'Ok'
        self.close()

    def cancel_clicked(self):
        self.close()

    def print_information(self, statistics):
        self.right_questions_nr.setStyleSheet('color:green')
        self.right_questions_nr.setText(str(statistics['right']))
        self.wrong_questions_nr.setStyleSheet('color:red')
        self.wrong_questions_nr.setText(str(statistics['wrong']))

        if statistics['accuracy'] > 0.5:
            color = f'green'
        else:
            color = f'red'
        self.accuracy.setStyleSheet(f'color:{color}')
        self.accuracy.setText(f'{str(statistics["accuracy"] * 100)}%')

        self.elapsed_time.setText(f'Rezolvarea testului a durat {str(statistics["time"]).split(".")[0]}')

    def show_result_window(self, statistics):
        self.print_information(statistics)
        self.exec_()
        return self.choice


class ExtendedQLabel(QLabel):
    def __init__(self):
        super(ExtendedQLabel, self).__init__()

    clicked = pyqtSignal(int)

    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.clicked.emit(int(self.text()))


class TestDialog(QDialog, test_dlg.Ui_Dialog):
    def __init__(self):
        super(TestDialog, self).__init__()
        self.setupUi(self)

        self.start_time = 0
        self.questions = None
        self.question_index = 0
        self.skipped_question_index = 0
        self.labels = []
        self.skipped_questions = []
        self.finished = False

        self.statistics = {
            'right': 0,
            'wrong': 0,
            'accuracy': 0.0,
            'time': 0
        }

        self.skip_btn.clicked.connect(self.skip)
        self.next_btn.clicked.connect(self.next)
        self.stop_btn.clicked.connect(self.stop)

    def stop(self):
        if not self.finished:
            message_window = QMessageBox()
            message_window.setIcon(QMessageBox.Warning)
            message_window.setWindowTitle('Atentie')
            message_window.setText('Nu ati rezolvat testul pana la sfarsit. '
                                   'Daca inchideti, progresul testului actual va fi pierdut')
            message_window.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            choice = message_window.exec_()
            if choice == QMessageBox.Ok:
                self.close()
        else:
            self.close()

    def populate_navbar(self):
        self.labels = [ExtendedQLabel() for _ in range(len(self.questions))]
        vbox = QHBoxLayout()
        self.nav_bar.setLayout(vbox)
        for label in self.labels:
            label.setStyleSheet('background-color : white')
            label.setText(str(self.labels.index(label) + 1))
            label.setAlignment(Qt.AlignCenter)
            label.setMinimumHeight(60)
            label.clicked.connect(self.determine_clicked_label)

            vbox.addWidget(label, stretch=1)

    def determine_clicked_label(self, value):
        if value - 1 in self.skipped_questions:
            self.reload_skipped_question(value)

    def reload_skipped_question(self, value):
        self.question_index = value - 1
        self.load_one()

    def skip(self):
        self.labels[self.question_index].setStyleSheet('background-color : gray')
        if self.question_index not in self.skipped_questions:
            self.skipped_questions.append(self.question_index)
        if self.increment_index():
            self.load_one()

    def increment_index(self):
        if self.finished:
            try:
                self.question_index = self.skipped_questions[self.skipped_question_index]
                if self.skipped_question_index + 1 < len(self.skipped_questions):
                    self.skipped_question_index += 1
                else:
                    self.skipped_question_index = 0
                return True
            except IndexError as e:
                # print(e)
                return False
        else:
            if self.question_index + 1 < len(self.questions):
                self.question_index += 1
                return True
            else:
                self.finished = True
            return False

    # def check_if_done2(self):
    #     if self.finished and len(self.skipped_questions) == 0:
    #         result = ResultWindow()
    #         print(result.show_result_window('tra'))
    #         # Calculate accuracy:
    #         self.statistics['accuracy'] = float((self.statistics['right'] /
    #                                             (self.statistics['right'] + self.statistics['wrong'])))
    #         self.statistics['time'] = datetime.now() - self.start_time
    #         message_window = QMessageBox()
    #         message_window.setIcon(QMessageBox.Information)
    #         message_window.setWindowTitle('Felicitari')
    #         message_window.setText(f'\tAti rezolvat acest test.\n'
    #                                f'Ati acumulat {self.statistics["right"]} raspunsuri corect si '
    #                                f'{self.statistics["wrong"]} raspunsuri gresite. \nInsusire intrebarilor'
    #                                f' este de {self.statistics["accuracy"]*100}%.\n'
    #                                f'Rezolvarea testului a durat {str(self.statistics["time"])}.')
    #         message_window.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #         choice = message_window.exec_()
    #         if choice == QMessageBox.Ok:
    #             self.close()

    def check_if_done(self):
        if self.finished and len(self.skipped_questions) == 0:

            self.statistics['accuracy'] = float((self.statistics['right'] /
                                                 (self.statistics['right'] + self.statistics['wrong'])))
            self.statistics['time'] = datetime.now() - self.start_time

            result_window = ResultWindow()
            choice = result_window.show_result_window(self.statistics)
            if choice == 'Ok':
                self.close()

    def next(self):
        if self.var_a.isChecked() or self.var_b.isChecked() or self.var_c.isChecked() or self.var_d.isChecked():
            if self.var_a.isChecked() and self.questions[self.question_index].get_answer() == 'a':
                self.labels[self.question_index].setStyleSheet('background-color : green')
                self.statistics['right'] += 1
            elif self.var_b.isChecked() and self.questions[self.question_index].get_answer() == 'b':
                self.labels[self.question_index].setStyleSheet('background-color : green')
                self.statistics['right'] += 1
            elif self.var_c.isChecked() and self.questions[self.question_index].get_answer() == 'c':
                self.labels[self.question_index].setStyleSheet('background-color : green')
                self.statistics['right'] += 1
            elif self.var_d.isChecked() and self.questions[self.question_index].get_answer() == 'c':
                self.labels[self.question_index].setStyleSheet('background-color : green')
                self.statistics['right'] += 1
            else:
                self.labels[self.question_index].setStyleSheet('background-color : red')
                self.statistics['wrong'] += 1

            if self.question_index in self.skipped_questions:
                self.skipped_questions.remove(self.question_index)
                if self.skipped_question_index > 0:
                    self.skipped_question_index -= 1
            if self.increment_index():
                self.load_one()

        else:
            message_window = QMessageBox()
            message_window.setIcon(QMessageBox.Warning)
            message_window.setWindowTitle('Atentie')
            message_window.setText('Nu ati selectat nici o varianta.')
            message_window.setStandardButtons(QMessageBox.Ok)
            message_window.exec_()
        self.check_if_done()

    def load_one(self):
        self.question_number.display(self.question_index + 1)
        self.load_question(self.questions[self.question_index])
        self.highlight_current_question_in_navbar()

    def highlight_current_question_in_navbar(self):
        self.labels[self.question_index].setStyleSheet('background-color : lightgray')

    def load_question(self, question):
        self.question_nr.setText(f'Intrebarea numarul {str(question.get_question_nr())} '
                                 f'din {question.get_domain_nr()} - {question.get_domain_name()}')
        self.question_text.clear()
        self.question_text.insertPlainText(question.get_question_text())
        variants = question.get_variants()
        self.var_a_text.clear()
        self.var_b_text.clear()
        self.var_c_text.clear()
        self.var_d_text.clear()
        self.var_a_text.insertPlainText(variants[0])
        self.var_b_text.insertPlainText(variants[1])
        self.var_c_text.insertPlainText(variants[2])
        self.var_d_text.insertPlainText(variants[3])

    def run_test(self, questions):
        self.start_time = datetime.now()
        self.questions = questions
        self.populate_navbar()
        self.load_one()
        self.exec_()
        return self.statistics


class Root(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Root, self).__init__(parent)
        self.setupUi(self)

        # Get the question from file.
        parser = question_parser.Parser()
        # Set up a statistics variable.
        self.statistics = {}
        self.domenii = []
        for i in range(4):
            parser.set_path(f'Domeniul_{i + 1}.txt', f'Answers_{i+1}.txt')
            parser.load_info()
            parser.process_info()
            parser.process_answers()
            self.domenii.append(question_parser.Domeniu(parser.get_info(), parser.get_answer_list()))
        for i in self.domenii:
            i.extract_questions()

        self.generate.clicked.connect(self.show_test_window)

    def check_selected_domains(self):
        dom_choices = []
        if self.dom_I.isChecked():
            dom_choices.append(self.domenii[0])
        if self.dom_II.isChecked():
            dom_choices.append(self.domenii[1])
        if self.dom_II.isChecked():
            dom_choices.append(self.domenii[2])
        if self.dom_IV.isChecked():
            dom_choices.append(self.domenii[3])
        return dom_choices

    def get_random_domain(self):
        choices = self.check_selected_domains()
        return random.choice(choices)

    def reset_extracted_questions_contor(self):
        for i in self.domenii:
            i.reset_extracted_question_contor()

    def get_questions(self, nr=1):
        questions = []
        for i in range(nr):
            domain = self.get_random_domain()
            questions.append(domain.get_random_question())
        self.reset_extracted_questions_contor()
        return questions

    def get_questions_number(self):
        if self.tests_20.isChecked():
            number = 20
        elif self.tests_30.isChecked():
            number = 30
        else:
            number = 40
        return number

    def show_test_window(self):
        questions = self.get_questions(self.get_questions_number())

        window = TestDialog()
        self.statistics = window.run_test(questions)
        # TODO: Show last test results in the main window.
        # TODO: Implement the inspector window.
        # TODO: Add the functionality to show the statistics graph.
        # TODO: Add the function to write and read internal data to file.


def main():
    application = QApplication(sys.argv)
    window = Root()
    window.show()
    application.exec_()


if __name__ == "__main__":
    main()
