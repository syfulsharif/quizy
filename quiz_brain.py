class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.qustion_list = q_list

    def next_question(self):
        current_question = self.qustion_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number} : {current_question.text} (True/False):  ")
