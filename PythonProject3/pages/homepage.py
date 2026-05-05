from math import floor

from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from matplotlib.dviread import Page
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from QuizBase.Question import Question
from customWidgets.ImageButton import ImageButton
from customWidgets.QuestionEdit import QuestionEdit
from customWidgets.QuizHome import quizinstance

from pages.pageBase import basePage

class HomePage(basePage):







    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        self.quizContainer = None
        self.createQuiz = None
        self.madeQuizs = None
        self.maxPerPage = 4
        self.currentPage = 0
        self.pageCount = 0

        self.Upbutton = None
        self.Downbutton = None

        self.pageNumber = None
        self.imageTest = None
        self.extraInfoButton = None
        self.extraInfoText = None
        self.infoOpen = False



    def setup(self,parent):
        super().setup(parent)
        if self.quizContainer != None:
            self.remove_widget(self.quizContainer)
        if self.createQuiz != None:
            self.remove_widget(self.createQuiz)

        self.quizContainer = GridLayout(cols=1, spacing=200, size_hint_y=None)

        self.quizContainer.center = (self.center_x, self.center_y+300)
        self.createQuiz = Button(text="Create New Quiz",size = (250,100))
        self.createQuiz.background_color = ((111/255)*2.5,(189/255)*2.5,(249/255)*2.5,1)
        self.createQuiz.center = (self.center_x+450, self.center_y-380)
        self.createQuiz.bind(on_press=self.toCreation)

        self.add_widget(self.createQuiz)
        self.pageCount = 0
        if len(parent.Quizzes) > 0:
            self.pageCount = floor((len(parent.Quizzes)-1)/self.maxPerPage)
            self.setupQuizlist()
        else:
            noQUiz = Label(text="There Appears to be no quizzes yet, Time to make some!\nlittle tip: its boring using one format for the whole quiz try to use differnt formats!")
            noQUiz.center = (self.center_x, self.center_y+100)
            noQUiz.color = (0.6,0.6,0.6,1)
            self.add_widget(noQUiz)


        self.add_widget(self.quizContainer)

        arrowSize = (50,50)
        buttonYoff = -400
        buttonWidth = 200
        if self.Upbutton != None:
            self.remove_widget(self.Upbutton)

        self.Upbutton = ImageButton("Images/arrowRight.png", size=arrowSize)
        self.Upbutton.background_color = ((111/255)*2.5,(189/255)*2.5,(249/255)*2.5,1)
        self.Upbutton.image.size = (30, 30)
        self.Upbutton.center_y += 10
        self.Upbutton.center = (self.center_x+buttonWidth/2, self.center_y+buttonYoff)
        self.Upbutton.bind(on_press=self.nextPage)
        self.add_widget(self.Upbutton)

        if self.Downbutton != None:
            self.remove_widget(self.Downbutton)
        self.Downbutton = ImageButton("Images/arrowLeft.png", size=arrowSize)
        self.Downbutton.background_color = ((111/255)*2.5,(189/255)*2.5,(249/255)*2.5,1)
        self.Downbutton.image.size = (30, 30)
        self.Downbutton.center_y += 10
        self.Downbutton.center = (self.center_x - buttonWidth / 2, self.center_y + buttonYoff)
        self.Downbutton.bind(on_press=self.prevPage)
        self.add_widget(self.Downbutton)
        if self.pageNumber != None:
            self.remove_widget(self.pageNumber)
        self.pageNumber = Label(text="1 / "+str(self.pageCount))
        self.pageNumber.center = (self.center_x, self.center_y + buttonYoff)
        self.pageNumber.color = (0,0,0,1)
        self.add_widget(self.pageNumber)

        self.extraInfoButton = Button(text="Extra Info",size = (100,50))
        self.extraInfoButton.center = (self.center_x-self.width/2-450, self.center_y + buttonYoff)
        self.extraInfoButton.bind(on_press=self.extraInfoSHow)
        self.add_widget(self.extraInfoButton)

    def extraInfoSHow(self,instance):
        self.infoOpen = not self.infoOpen
    def nextPage(self,instance):
        self.currentPage += 1
        if self.currentPage > (self.pageCount):
            self.currentPage = 0
        self.setupQuizlist(self.currentPage)
    def prevPage(self,instance):
        self.currentPage -= 1
        if self.currentPage < 0:
            self.currentPage = self.pageCount
            if self.currentPage < 0:
                self.currentPage = 0
        self.setupQuizlist(self.currentPage)
    def setupQuizlist(self,newPage=0):
        if self.madeQuizs is not None:
            for q in self.madeQuizs:
                self.quizContainer.remove_widget(q)
        self.madeQuizs = []
        self.currentPage = newPage

        currentpageIndex = newPage * self.maxPerPage
        for index in range(currentpageIndex,currentpageIndex + (self.maxPerPage)):
            if index < len(self.Parent.Quizzes):
                newQuizSheet = quizinstance(self.Parent,index, self.Parent.Quizzes[index])
                newQuizSheet.center = self.center
                newQuizSheet.Setup()
                self.madeQuizs.append(newQuizSheet)
                self.quizContainer.add_widget(newQuizSheet)



    def toCreation(self,instance):
        self.parent.switchPage(1)

    def updatePage(self):
        self.pageNumber.text = str(self.currentPage+1) + " / " + str(self.pageCount+1)
        foundOneToKill = False
        killList = []
        if len(self.Parent.Quizzes) > 0:
            for q in self.madeQuizs:
                q.updateIcons()
                if q.killme:
                    foundOneToKill = True
                    killList.append(q.instanceID)

        if foundOneToKill:
           for index in killList:
               self.parent.Quizzes.pop(index)
           self.setup(self.Parent)


        if self.infoOpen and self.extraInfoText == None:
            self.extraInfoText = Label(text="Quizzes made: " + str(len(self.parent.Quizzes)))
            self.extraInfoText.center = (self.center_x-self.width/2-450, self.center_y -350)
            self.extraInfoText.color = (0.6,0.6,0.6,1)
            self.add_widget(self.extraInfoText)
        if not self.infoOpen and self.extraInfoText != None:
            self.remove_widget(self.extraInfoText)
            self.extraInfoText = None


