class QuestionAnswerRules:
    def __init__(self, question_list):
        self.list_of_question = question_list
        self.number_of_question = 0
        self.points = 0

    def following_question(self):
        current_question = self.list_of_question[self.number_of_question]
        self.number_of_question += 1
        user_answer = input(f"Q.{self.number_of_question} {current_question.question_t} (True/False)").lower()
        self.check_answer(user_answer, current_question.answer_t)

    def test_finish(self):
        return self.number_of_question < len(self.list_of_question)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.points += 1
            print(f"Your answer is correct and your score is {self.points}. ")
        else:
            print(f"Your answer is wrong and your score is {self.points}. ")
        print(f"Your current score is {self.points}. ")

