class Question:
    def __init__(self, question_text):
        self.question_text = question_text
        self.answers = []
        self.answer_index = 0
        self.textFormatAnswer = ""
        self.formatType = 0
        self.randomized = True
        self.image = ""
    def set_question_text(self, question_text):
        self.question_text = question_text

    def set_format(self, format_type):
        self.formatType = format_type
    def add_answer(self, answer):
        self.answers.append(answer)
    def remove_answer(self, answerIndex):
        self.answers.remove(self.answers[answerIndex])
