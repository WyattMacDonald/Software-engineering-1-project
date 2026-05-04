from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from matplotlib.dviread import Page
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from customWidgets.AnswerInstance import AnswerEditInstance
from customWidgets.ImageButton import ImageButton


class QuizAnswerMulti(Widget):
    def __init__(self):
        super(QuizAnswerMulti, self).__init__()
        self.label = None
        self.button = None
        self.RepersentedAnswer = -1
        self.index = -1
        self.selected = False
        self.timer = 0
        self.savedAnswer = ""

    sizeX = NumericProperty(0)
    sizeY = NumericProperty(0)
    posX = NumericProperty(0)
    posY = NumericProperty(0)

    def updateProperties(self):
        self.sizeX = 600
        self.sizeY = 80
        self.posX = self.center_x
        self.posY = self.center_y
    def setup(self,index,realAnswer,answer):
        self.index = index
        self.RepersentedAnswer = realAnswer
        self.savedAnswer = answer
        if self.label is not None:
            self.remove_widget(self.label)
        if self.button is not None:
            self.remove_widget(self.button)

        letter = chr(ord('A')+index)

        self.label = Label(text=(letter + ". "+answer))
        self.label.halign = "left"
        self.label.valign = "center"
        self.label.text_size = (300,100)

        self.add_widget(self.label)

        self.button = ImageButton("Images/selectionFilled.png",size = (50,50))
        self.button.bind(on_press=self.press)
        self.button.background_color = (1,1,1,0)

        self.add_widget(self.button)
    def press(self,instance):
        self.selected = True

    def update(self):
        self.updateProperties()
        self.button.center = (self.center_x+200, self.center_y)
        self.label.center = (self.center_x-100, self.center_y)
        if self.selected:
            self.timer += 1
            self.button.image.source = "Images/selectionFilled.png"
        else:
            self.timer = -1
            self.button.image.source = "Images/selectionNonFilled.png"








