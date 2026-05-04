class quiz:
    def __init__(self,name):
        self.questions = []
        self.name = name
        self.score = 0

    def addQuestion(self, question):
        self.questions.append(question)
