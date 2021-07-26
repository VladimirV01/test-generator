import random


class Parser:
    def __init__(self, path=None, answers_path=None):
        self.path = path
        self.answers_path = answers_path
        self.info = None
        self.answer_list = []

    def set_path(self, path, answers_path):
        self.path = path
        self.answers_path = answers_path

    def load_info(self):
        with open(self.path, 'r') as file:
            lines = file.readlines()
        self.info = lines

    def process_info(self):
        # Remove newlines from the list
        while '\n' in self.info:
            self.info.remove('\n')

        # Replace tabs in the strings with simple spaces
        for i in range(len(self.info)):
            self.info[i] = self.info[i].replace('\t', ' ')

    def process_answers(self):
        with open(self.answers_path, 'r') as file:
            answers = file.readlines()
        for i in answers:
            self.answer_list.append(i.split(' ')[1].replace('\n', ''))

    def get_info(self):
        return self.info

    def get_answer_list(self):
        return self.answer_list


class Domeniu:
    def __init__(self, info, answer_list):
        self.domain_nr = info[0].replace('\n', '')
        self.domain_name = info[1].replace('\n', '')
        self.info = info[2:]
        self.answer_list = answer_list

        self.questions = []
        self.extracted_questions = []

    def extract_questions(self):
        index = 0
        while index < len(self.info):
            try:
                if int(self.info[index][0]) in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                    new_question = self.Question(self.info[index],
                                                 self.info[index + 1],
                                                 self.info[index + 2],
                                                 self.info[index + 3],
                                                 self.info[index + 4],
                                                 self.domain_nr,
                                                 self.domain_name,
                                                 self.answer_list)
                    self.questions.append(new_question)
                    index += 5
            except ValueError:
                index += 1

    def get_random_question(self):

        question = random.choice(self.questions)
        while question.get_question_nr() in self.extracted_questions:
            question = random.choice(self.questions)

        self.extracted_questions.append(question.get_question_nr())
        return question

    def get_specific_question(self, nr):
        for question in self.questions:
            if question.get_question_nr() == nr:
                return question

    def get_extracted_question_list(self):
        return self.extracted_questions

    def reset_extracted_question_contor(self):
        self.extracted_questions = []

    def get_all_questions(self):
        return self.questions

    def get_domain_name(self):
        return self.domain_name

    def get_domain_nr(self):
        return self.domain_nr

    def get_domain_name_nr(self):
        return self.domain_nr, self.domain_name

    class Question:
        def __init__(self, text, var_a, var_b, var_c, var_d, domain_nr, domain_name, answers):
            self.question_text = text
            self.question_nr = None
            self.domain_nr = domain_nr
            self.domain_name = domain_name
            self.extract_question_number()
            # Slice the first 3 chars from the variants. Those chars are a), b), c), d).
            self.var_a = var_a[3:]
            self.var_b = var_b[3:]
            self.var_c = var_c[3:]
            self.var_d = var_d[3:]

            self.answer = None
            self.answers = answers
            self.find_answer()

        def find_answer(self):
            self.answer = self.answers[self.question_nr - 1]

        def extract_question_number(self):
            char_nr = ''
            for i in range(len(self.question_text)):
                if self.question_text[i] != '.':
                    # Collect the string containing question number until '.' found which states for the delimitation
                    # of the question number.
                    char_nr += self.question_text[i]
                elif self.question_text[i] == '.':
                    # Convert the collected question number from string to number.
                    self.question_nr = int(char_nr)
                    # Slice the number from the question text.
                    self.question_text = self.question_text[(i + 2):]
                    break

        def set_domain_nr(self, info):
            self.domain_nr = info

        def get_domain_nr(self):
            return self.domain_nr

        def set_domain_name(self, info):
            self.domain_name = info

        def get_domain_name(self):
            return self.domain_name

        def set_right_answer(self, answer):
            self.answer = answer

        def get_question_text(self):
            return self.question_text

        def get_variants(self):
            return self.var_a, self.var_b, self.var_c, self.var_d

        def get_answer(self):
            return self.answer

        def get_question_nr(self):
            return self.question_nr

        def print_question(self):
            print(f'Question number {self.question_nr}: {self.question_text}')
            print(f'a) {self.var_a}')
            print(f'b) {self.var_b}')
            print(f'c) {self.var_c}')
            print(f'd) {self.var_d}')
            print(f'Answer: {self.answer}')


if __name__ == "__main__":
    parser = Parser('Domeniul_1.txt', 'Answers_1.txt')
    parser.load_info()
    parser.process_info()
    parser.process_answers()
    dom1 = Domeniu(parser.get_info(), parser.get_answer_list())
    dom1.extract_questions()
    dom1.get_random_question().print_question()
    dom1.get_specific_question(57).print_question()

    # parser.set_path('Domeniul_2.txt')
    # parser.load_info()
    # parser.process_info()
    # parser.process_answers()
    # dom2 = Domeniu(parser.get_info(), parser.get_answer_list())
    # dom2.extract_questions()
    # dom2.get_random_question().print_question()
    # dom2.get_specific_question(24).print_question()




