from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from matplotlib.dviread import Page
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from QuizBase.Question import Question
from customWidgets.ImageButton import ImageButton
from customWidgets.QuestionEdit import QuestionEdit

from pages.pageBase import basePage
from QuizBase.Quiz import quiz

class createQuiz(basePage):

    def __init__(self, **kwargs):
        super(createQuiz, self).__init__(**kwargs)
        self.tests = []

        self.newQuestionButton = None

        self.currentQuestionIndex = 0

        self.currentTest = None

        self.quizName = None

        self.upArrow = None
        self.downArrow = None

        self.quizInfo = None
        self.impQuiz = None


    def setup(self,parent):
        super().setup(parent)

        self.newQuestionButton = Button(text="New Question")
        self.newQuestionButton.bind(on_press=self.newQuestion)
        self.newQuestionButton.center = (self.center_x - (parent.width / 2) + 50,
                                         self.center_y - (parent.height / 2) + 50)
        self.newQuestionButton.size = (200, 60)
        self.newQuestionButton.background_color =  ((111/255)*2.5,(189/255)*2.5,(249/255)*2.5,1)
        self.add_widget(self.newQuestionButton)

        self.quizName = TextInput(size = (200,50), multiline = False)
        self.quizName.center = (self.center_x - (parent.width / 2) + 130,self.center_y + (parent.height / 2) -350)

        quizlabel = Label(text = "Quiz's Name here:")
        quizlabel.center = (self.center_x - (parent.width / 2) + 130,self.center_y + (parent.height / 2) -300)
        quizlabel.color = (0.2,0.2,0.2,1)
        self.add_widget(quizlabel)

        arrowSize = (40,40)

        arrowYoff = 20

        self.upArrow = ImageButton("Images/arrowRight.png",size = arrowSize)
        self.upArrow.image.size = (30,30)
        self.upArrow.center_y += 10
        self.upArrow.background_color =  ((111/255)*2.5,(189/255)*2.5,(249/255)*2.5,1)
        self.upArrow.bind(on_press=self.upQuestion)
        self.upArrow.center = (parent.center_x+100, parent.center_y - (parent.height/2)+arrowYoff)
        self.add_widget(self.upArrow)

        self.downArrow = ImageButton("Images/arrowLeft.png",size = arrowSize)
        self.downArrow.image.size = (30,30)
        self.downArrow.center_y += 10
        self.downArrow.background_color =  ((111/255)*2.5,(189/255)*2.5,(249/255)*2.5,1)
        self.downArrow.bind(on_press=self.downQuestion)
        self.downArrow.center = (parent.center_x - 100, parent.center_y - (parent.height/2)+arrowYoff)
        self.add_widget(self.downArrow)

        self.quizInfo = Label(text = "1 / 1")
        self.quizInfo.center = (parent.center_x, parent.center_y - (parent.height/2)+arrowYoff)
        self.quizInfo.color = (0,0,0,1)
        self.add_widget(self.quizInfo)

        self.impQuiz = Button(text = "Submit")
        self.impQuiz.center = (parent.center_x+(parent.width/2)-150, parent.center_y - (parent.height/2)+50)
        self.impQuiz.size = (200,60)
        self.impQuiz.background_color =  ((111/255)*2.5,(189/255)*2.5,(249/255)*2.5,1)
        self.impQuiz.bind(on_press=self.createNewQuiz)

        self.add_widget(self.impQuiz)

        self.add_widget(self.quizName)

        self.newQuestion(None)


    def createNewQuiz(self,instance):

        if (self.currentIndexNotfinished != -1 or self.quizName.text == ""):
            if self.currentIndexNotfinished != -1:
                self.changeQuestion(self.currentIndexNotfinished)

            return
        newQuiz = quiz(self.quizName.text)
        for test in self.tests:
            test.updateQuestion()
            question = test.inputedQuestion
            newQuiz.addQuestion(question)

        self.parent.Quizzes.append(newQuiz)
        self.remove_widget(self.currentTest)
        self.tests = []
        self.parent.switchPage(0)





    def upQuestion(self,instance):
        newindex = self.currentQuestionIndex+1
        if newindex > len(self.tests)-1:
            newindex = 0
        self.changeQuestion(newindex)
    def downQuestion(self,instance):
        newindex = self.currentQuestionIndex-1
        if newindex < 0:
            newindex = len(self.tests)-1
        self.changeQuestion(newindex)


    def changeQuestion(self,index):
        self.remove_widget(self.currentTest)
        self.currentQuestionIndex = index
        self.currentTest = self.tests[index]
        self.add_widget(self.currentTest)
        self.quizInfo.text = str(index+1) + " / "+ str(len(self.tests))

    def newQuestion(self,instance):
        testQuestion = Question("t")
        testQuestion.add_answer("")

        newQuestionEdit = QuestionEdit()
        newQuestionEdit.updateSelf( len(self.tests),testQuestion)

        self.remove_widget(self.currentTest)

        self.currentTest = newQuestionEdit
        self.currentTest.center = self.center
        self.tests.append(newQuestionEdit)
        self.add_widget(self.currentTest)




        self.currentQuestionIndex = len(self.tests)-1
        self.quizInfo.text = str(self.currentQuestionIndex + 1) + " / " + str(len(self.tests))



    currentIndexNotfinished = -1
    def updatePage(self):
       super().updatePage()
       self.currentIndexNotfinished = -1
       removeList = []
       removedSomething = False
       removedCurrentQuestion = False

       for test in self.tests:
           test.updateandCheckQuestions()
           if not test.checkIfFinished():
               if self.currentIndexNotfinished == -1:
                   self.currentIndexNotfinished = test.whoAmI
           if test.RemoveMe:
               removedSomething = True
               removeList.append(test.whoAmI)

       for index in removeList:
           if index == self.currentQuestionIndex:
               removedCurrentQuestion = True
           self.tests.pop(index)
       if removedCurrentQuestion:
            self.changeQuestion(self.currentQuestionIndex-1)




