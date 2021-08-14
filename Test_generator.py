import pickle
import random
import sys
from datetime import datetime

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLabel, QHBoxLayout, QMessageBox
import matplotlib.pyplot as plt

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

    def print_information(self, record):
        self.right_questions_nr.setStyleSheet('color:green')
        self.right_questions_nr.setText(str(record.get_right_answers()))
        self.wrong_questions_nr.setStyleSheet('color:red')
        self.wrong_questions_nr.setText(str(record.get_wrong_answers()))

        if record.get_accuracy() > 0.5:
            color = f'green'
        else:
            color = f'red'
        self.accuracy.setStyleSheet(f'color:{color}')
        self.accuracy.setText(f'{str(record.get_accuracy() * 100)}%')

        self.elapsed_time.setText(f'Rezolvarea testului a durat {str(record.get_elapsed_time()).split(".")[0]}')

    def show_result_window(self, record):
        self.print_information(record)
        self.exec_()
        return self.choice


class ExtendedQLabel(QLabel):
    def __init__(self):
        super(ExtendedQLabel, self).__init__()

    clicked = pyqtSignal(int)

    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.clicked.emit(int(self.text()))


class Statistics:
    def __init__(self):
        self.records = []
        self.added_new_record = False

    def add_record(self, right_answers=0, start_time=0, nr_questions=0):
        self.records.append(self.Record(right_answers, start_time, nr_questions))
        self.added_new_record = True

    def add_record_object(self, record_object):
        self.records.append(record_object)
        self.added_new_record = True

    def get_last_record(self):
        try:
            return self.records[len(self.records) - 1]
        except IndexError:
            print(f'No records.')

    def get_records(self):
        return self.records

    def delete_records(self):
        self.records = []

    def exist_new_records(self):
        return self.added_new_record

    def collect_data_and_draw_graph(self):
        if len(self.records) > 0:
            y_values = [self.records[i].get_accuracy() * 100 for i in range(len(self.records))]
            x_values = [x for x in range(len(self.records))]
            plt.plot(x_values, y_values)
            plt.ylabel('Rezultatele testelor (%)')
            plt.xlabel('Numarul inregistrarii')

            plt.title('Statistica rezolvarii testelor')
            plt.show()

    class Record:
        def __init__(self, right_answers=0, start_time=0, nr_questions=0):
            self.right_answers = right_answers
            self.datetime = start_time
            self.nr_questions = nr_questions
            self.wrong_answers = 0
            self.accuracy = 0.0
            self.elapsed_time = 0
            self.complete_record = False
            self.selected_domains = []
            if self.right_answers and self.datetime and self.nr_questions:
                self.finished_record()

        def set_selected_domains(self, domains):
            self.selected_domains = domains

        def set_right_answers(self, right_answers=0):
            self.right_answers = right_answers

        def increment_right_answers(self):
            self.right_answers += 1

        def set_start_time(self):
            self.datetime = datetime.now()

        def set_nr_questions(self, nr_questions):
            self.nr_questions = nr_questions

        def finished_record(self):
            self.wrong_answers = self.nr_questions - self.right_answers
            self.accuracy = round(float(self.right_answers / self.nr_questions), 2)
            self.elapsed_time = datetime.now() - self.datetime
            self.complete_record = True

        def print_record(self):
            print(self.get_record_info())

        def get_record_info(self):
            return f'This test of {self.nr_questions} questions was taken {self.datetime}.\n' \
                   f'The selected domains were {*self.selected_domains,}.\n' \
                   f'There were accumulated {self.right_answers} right answers and {self.wrong_answers} ' \
                   f'wrong answers.\nThe accuracy was {self.accuracy * 100}%.\n'\
                   f'The test was completed in {self.elapsed_time}.'

        def get_right_answers(self):
            return self.right_answers

        def get_wrong_answers(self):
            return self.nr_questions - self.right_answers

        def get_accuracy(self):
            return self.accuracy

        def get_nr_questions(self):
            return self.nr_questions

        def get_elapsed_time(self):
            return self.elapsed_time

        def get_datetime(self):
            return self.datetime

        def get_complete_record_status(self):
            return self.complete_record

        def __repr__(self):
            return self.get_record_info()


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

        self.skip_btn.clicked.connect(self.skip)
        self.next_btn.clicked.connect(self.next)
        self.stop_btn.clicked.connect(self.stop)
        self.answer.clicked.connect(self.show_result)

        for var in ('a', 'b', 'c', 'd'):
            textfield = eval(f'self.var_{var}_text')
            textfield.setContextMenuPolicy(Qt.CustomContextMenu)
            textfield.mousePressEvent = eval(f'self.var_{var}_click')
            textfield.mouseDoubleClickEvent = eval(f'self.var_{var}_doubleclick')

    def var_a_click(self, event):
        if event.button() == Qt.RightButton and not self.answer.isEnabled():
            self.next()
        elif event.button() == Qt.LeftButton and self.answer.isEnabled():
            self.var_a.setChecked(True)

    def var_b_click(self, event):
        if event.button() == Qt.RightButton and not self.answer.isEnabled():
            self.next()
        elif event.button() == Qt.LeftButton and self.answer.isEnabled():
            self.var_b.setChecked(True)

    def var_c_click(self, event):
        if event.button() == Qt.RightButton and not self.answer.isEnabled():
            self.next()
        elif event.button() == Qt.LeftButton and self.answer.isEnabled():
            self.var_c.setChecked(True)

    def var_d_click(self, event):
        if event.button() == Qt.RightButton and not self.answer.isEnabled():
            self.next()
        elif event.button() == Qt.LeftButton and self.answer.isEnabled():
            self.var_d.setChecked(True)

    def var_a_doubleclick(self, event):
        if event.button() == Qt.LeftButton and self.answer.isEnabled():
            self.var_a.setChecked(True)
            self.show_result()

    def var_b_doubleclick(self, event):
        if event.button() == Qt.LeftButton and self.answer.isEnabled():
            self.var_b.setChecked(True)
            self.show_result()

    def var_c_doubleclick(self, event):
        if event.button() == Qt.LeftButton and self.answer.isEnabled():
            self.var_c.setChecked(True)
            self.show_result()

    def var_d_doubleclick(self, event):
        if event.button() == Qt.LeftButton and self.answer.isEnabled():
            self.var_d.setChecked(True)
            self.show_result()

    def show_result(self):
        if self.check_if_anything_anything_is_selected():
            answer, _ = self.check_selected_answer()
            if answer == self.questions[self.question_index].get_answer():
                textfield = eval(f'self.var_{answer}_text')
                textfield.setStyleSheet('background-color:green')
            else:
                right_textfield = eval(f'self.var_{self.questions[self.question_index].get_answer()}_text')
                right_textfield.setStyleSheet('background-color:green')
                wrong_textfield = eval(f'self.var_{answer}_text')
                wrong_textfield.setStyleSheet('background-color:red')

            if self.question_index in self.skipped_questions:
                self.skipped_questions.remove(self.question_index)
                if self.skipped_question_index > 0:
                    self.skipped_question_index -= 1

            if (self.question_index == len(self.questions) - 1 and len(self.skipped_questions) == 0) or \
                    (self.finished and len(self.skipped_questions) == 0):
                self.next_btn.setText('Termina testul')

            self.next_btn.setEnabled(True)
            self.toggle_answers_enabled(state=False)
            self.skip_btn.setEnabled(False)
            self.answer.setEnabled(False)

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
        if self.finished:
            self.question_index = value - 1
            self.load_one()
        else:
            message_window = QMessageBox()
            message_window.setIcon(QMessageBox.Warning)
            message_window.setWindowTitle('Atentie')
            message_window.setText('Mai întâi răspundeți la toate întrebările apoi puteți reveni la cele sărite.')
            message_window.setStandardButtons(QMessageBox.Ok)
            message_window.exec_()

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
                return self.increment_index()

    def check_if_done(self):
        if self.finished and len(self.skipped_questions) == 0:
            self.record.finished_record()
            result_window = ResultWindow()
            choice = result_window.show_result_window(self.record)
            if choice == 'Ok':
                self.close()

    def set_right_label(self):
        self.labels[self.question_index].setStyleSheet('background-color : green')

    def set_wrong_label(self):
        self.labels[self.question_index].setStyleSheet('background-color : red')

    def check_selected_answer(self):
        for var in ('a', 'b', 'c', 'd'):
            if eval(f'self.var_{var}.isChecked()'):
                if self.questions[self.question_index].get_answer() == var:
                    return var, True
                break
        return var, False

    def toggle_answers_enabled(self, state=None):
        if state is None:
            if self.var_a.isEnabled():
                state = False
            else:
                state = True
        for i in ('a', 'b', 'c', 'd'):
            check = eval(f'self.var_{i}')
            check.setEnabled(state)

    def deselect_answers(self):
        for i in ('a', 'b', 'c', 'd'):
            check = eval(f'self.var_{i}')
            check.setAutoExclusive(False)
            check.setChecked(False)
            check.setAutoExclusive(True)

    def reset_var_background(self):
        for var in ('a', 'b', 'c', 'd'):
            textfield = eval(f'self.var_{var}_text')
            textfield.setStyleSheet('background-color:white')

    def check_if_anything_anything_is_selected(self):
        if self.var_a.isChecked() or self.var_b.isChecked() or self.var_c.isChecked() or self.var_d.isChecked():
            return True
        else:
            message_window = QMessageBox()
            message_window.setIcon(QMessageBox.Warning)
            message_window.setWindowTitle('Atentie')
            message_window.setText('Nu ati selectat nici o varianta.')
            message_window.setStandardButtons(QMessageBox.Ok)
            message_window.exec_()
            return False

    def next(self):
        if self.check_if_anything_anything_is_selected():
            _, correct = self.check_selected_answer()
            if correct:
                self.set_right_label()
                self.record.increment_right_answers()
            else:
                self.set_wrong_label()

            if self.increment_index():
                self.load_one()

        self.check_if_done()

    def load_one(self):
        self.question_number.display(self.question_index + 1)
        self.load_question(self.questions[self.question_index])
        self.highlight_current_question_in_navbar()
        self.next_btn.setEnabled(False)
        self.deselect_answers()
        self.toggle_answers_enabled(state=True)
        self.reset_var_background()
        self.skip_btn.setEnabled(True)
        self.answer.setEnabled(True)

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

    def run_test(self, questions, record):
        self.record = record
        self.record.set_start_time()
        self.record.set_nr_questions(len(questions))
        self.record.set_right_answers()

        self.questions = questions
        self.populate_navbar()
        self.load_one()
        self.exec_()
        return self.record


class Root(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Root, self).__init__(parent)
        self.setupUi(self)

        # Get the question from file.
        parser = question_parser.Parser()
        # Set up a statistics variable. Try to read it from file first.
        try:
            with open('config.statistics', 'rb') as config_stats_file:
                self.statistics = pickle.load(config_stats_file)
                self.load_last_test_statistics()
        except FileNotFoundError:
            self.statistics = Statistics()

        self.domenii = []
        for i in range(4):
            parser.set_path(f'Domeniul_{i + 1}.txt', f'Answers_{i + 1}.txt')
            parser.load_info()
            parser.process_info()
            parser.process_answers()
            self.domenii.append(question_parser.Domeniu(parser.get_info(), parser.get_answer_list()))
        for i in self.domenii:
            i.extract_questions()

        self.show_statistics.clicked.connect(self.statistics.collect_data_and_draw_graph)
        self.generate.clicked.connect(self.show_test_window)

    def load_last_test_statistics(self):
        record = self.statistics.get_last_record()
        self.last_test_datetime.setDateTime(record.get_datetime())
        if record.get_accuracy() < 0.5:
            color = 'red'
        else:
            color = 'green'
        self.last_test_accuracy.setStyleSheet(f'color:{color}; font-size:25px')
        self.last_test_accuracy.setText(f'{str(record.get_accuracy() * 100)}%')
        self.last_test_right_answers.setStyleSheet('color:green; font-size:25px')
        self.last_test_right_answers.setText(str(record.get_right_answers()))
        self.last_test_wrong_answers.setStyleSheet('color:red; font-size:25px')
        self.last_test_wrong_answers.setText(str(record.get_wrong_answers()))
        self.last_test_duration.setText(str(record.get_elapsed_time()).split('.')[0])

    def check_selected_domains(self):
        dom_choices = []
        if self.dom_I.isChecked():
            dom_choices.append(self.domenii[0])
        if self.dom_II.isChecked():
            dom_choices.append(self.domenii[1])
        if self.dom_III.isChecked():
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
        record = window.run_test(questions, self.statistics.Record())
        record.set_selected_domains([name.get_domain_name_nr() for name in self.check_selected_domains()])

        if record.get_complete_record_status():
            self.statistics.add_record_object(record)
        self.load_last_test_statistics()

    def save_statistics(self):
        with open('config.statistics', 'wb') as config_stats_file:
            pickle.dump(self.statistics, config_stats_file)

    def closeEvent(self, event):
        if self.statistics.added_new_record:
            self.save_statistics()
        event.accept()


def main():
    application = QApplication(sys.argv)
    window = Root()
    window.show()
    application.exec_()


if __name__ == "__main__":
    main()
