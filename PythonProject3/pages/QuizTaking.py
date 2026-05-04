from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from customWidgets.ImageButton import ImageButton
from customWidgets.QuestionInstance import questionInstance
from pages.pageBase import basePage


class quizTaking(basePage):
    def __init__(self, **kwargs):
        super(quizTaking, self).__init__(**kwargs)
        self.questions = []



        self.currentQuestionIndex = 0

        self.currentquestion = None

        self.quizName = None

        self.upArrow = None
        self.downArrow = None

        self.quizInfo = None
        self.finishQuizButton = None

        self.theQuiz = None

    def testText(self):
        return "wtf"
    def setup(self,parent):
        print("setup")
        super().setup(parent)

        self.theQuiz = parent.Quizzes[parent.currentQuizindex]




        self.quizName = Label(text = self.theQuiz.name)

        self.quizName.center = (self.center_x - (parent.width / 2) + 130,self.center_y + (parent.height / 2) -350)

        arrowSize = (40,40)

        arrowYoff = 20

        self.upArrow = ImageButton("Images/arrowRight.png", size=arrowSize)
        self.upArrow.image.size = (30, 30)
        self.upArrow.center_y += 10
        self.upArrow.background_color =  ((111/255)*2.5,(189/255)*2.5,(249/255)*2.5,1)
        self.upArrow.bind(on_press=self.upQuestion)
        self.upArrow.center = (parent.center_x+50, parent.center_y - (parent.height/2)+arrowYoff)
        self.add_widget(self.upArrow)

        self.downArrow = ImageButton("Images/arrowLeft.png", size=arrowSize)
        self.downArrow.image.size = (30, 30)
        self.downArrow.center_y += 10
        self.downArrow.background_color =  ((111/255)*2.5,(189/255)*2.5,(249/255)*2.5,1)
        self.downArrow.bind(on_press=self.downQuestion)
        self.downArrow.center = (parent.center_x - 50, parent.center_y - (parent.height/2)+arrowYoff)
        self.add_widget(self.downArrow)

        self.quizInfo = Label(text = "1 / 1")
        self.quizInfo.center = (parent.center_x, parent.center_y - (parent.height/2)+arrowYoff)
        self.quizInfo.color = (1,0,0,1)
        self.add_widget(self.quizInfo)

        self.finishQuizButton = Button(text = "Submit")
        self.finishQuizButton.center = (parent.center_x+(parent.width/2)-100, parent.center_y - (parent.height/2)+200)
        self.finishQuizButton.bind(on_press=self.finish)

        self.add_widget(self.finishQuizButton)

        self.add_widget(self.quizName)

        self.setupQuestions()


    def finish(self,instance):
        correctAmount = 0
        for question in self.questions:
            if question.amIcorrect():
                correctAmount += 1
        self.parent.Quizzes[self.parent.currentQuizindex].score = correctAmount
        self.parent.switchPage(0)




    def setupQuestions(self):
        i = 0
        for question in self.theQuiz.questions:
            newQuestion = questionInstance()
            newQuestion.setup(i, question)
            newQuestion.center = self.center
            self.questions.append(newQuestion)
            i += 1
        self.changeQuestion(0)

    def upQuestion(self,instance):
        newindex = self.currentQuestionIndex+1
        if newindex > len(self.questions)-1:
            newindex = 0
        self.changeQuestion(newindex)
    def downQuestion(self,instance):
        newindex = self.currentQuestionIndex-1
        if newindex < 0:
            newindex = len(self.questions)-1
        self.changeQuestion(newindex)


    def changeQuestion(self,index):
        if self.currentquestion != None:
            self.remove_widget(self.currentquestion)
        self.currentQuestionIndex = index
        self.currentquestion = self.questions[index]

        self.add_widget(self.currentquestion)
        self.quizInfo.text = str(index+1) + " / "+ str(len(self.questions))





    currentIndexNotfinished = -1
    def updatePage(self):

       self.currentIndexNotfinished = -1

       for question in self.questions:
           question.update()


