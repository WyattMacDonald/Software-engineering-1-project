from kivy.properties import NumericProperty
from kivy.uix.button import Button
from matplotlib.dviread import Page
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from customWidgets.ImageButton import ImageButton


class quizinstance(Widget):

    def __init__(self,parent,id,quiz,**kwargs):
        super(quizinstance, self).__init__(**kwargs)
        self.inputedQuiz = quiz
        self.instanceID = id
        self.QuizName = None
        self.QuizScore = None
        self.takeQuiz = None
        self.percentage = None
        self.killButton = None
        self.killme = False

        self.Parent = parent


    def Setup(self):

        if self.QuizName != None:
            self.remove_widget(self.QuizName)
        self.QuizName = Label(text=self.inputedQuiz.name)
        self.QuizName.halign = 'left'
        self.QuizName.valign = 'center'
        self.QuizName.text_size = (500,500)
        self.QuizName.color = (0.2,0.2,0.2,1)
        self.QuizName.font_size = 40
        self.QuizName.center = (self.center_x-600, self.center_y-100)
        if self.QuizScore != None:
            self.remove_widget(self.QuizScore)
        self.QuizScore = Label(text=(str(self.inputedQuiz.score)+" / "+str(len(self.inputedQuiz.questions))))
        self.QuizScore.center = self.center
        self.QuizScore.color = (0.2,0.2,0.2,1)
        self.QuizScore.font_size = 30

        percent = self.inputedQuiz.score / len(self.inputedQuiz.questions)

        self.percentage = Label(text= str(round(percent*100)) + "%")
        self.percentage.font_size = 40
        self.percentage.color =  (0.2,0.2,0.2,1)
        self.add_widget(self.percentage)


        if (self.takeQuiz != None):
            self.remove_widget(self.takeQuiz)
        self.takeQuiz = Button(text="Take Quiz",size = (150,50))
        self.takeQuiz.bind(on_press = self.takeQUIZ)
        self.takeQuiz.background_color = ((111/255)*1.1,(189/255)*1.1,(249/255)*1.1,1)
        self.add_widget(self.takeQuiz)

        self.killButton = ImageButton("Images/trash.png",size = (50,50))
        self.killButton.background_color =  ((111/255)*1.1,(189/255)*1.1,(249/255)*1.1,1)
        self.killButton.bind(on_press = self.kill)


        self.add_widget(self.killButton)



        self.add_widget(self.QuizName)
        self.add_widget(self.QuizScore)
    def kill(self,instance):
        self.killme = True
    sizeX = NumericProperty(0)
    sizeY = NumericProperty(0)
    posX = NumericProperty(0)
    posY = NumericProperty(0)
    def takeQUIZ(self,instance):
        parent = self.Parent
        parent.currentQuizindex = self.instanceID
        parent.switchPage(2)

    def updateProperties(self):
        self.sizeX = 700
        self.sizeY = 180
        self.posX = self.center_x
        self.posY = self.center_y
    def updateIcons(self):
        self.QuizName.center = (self.center_x-80, self.center_y+65 )
        self.QuizScore.center = self.center
        self.percentage.center = (self.center_x-100, self.center_y )
        self.takeQuiz.center = (self.center_x+(self.sizeX/2)-80, self.center_y-(self.sizeY/2)+30)
        self.killButton.center = (self.center_x+(self.sizeX/2)-25, self.center_y+(self.sizeY/2)-25)
        self.updateProperties()
