from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from matplotlib.dviread import Page
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from customWidgets.AnswerInstance import AnswerEditInstance

class Dropdown(Widget):
    def __init__(self,options, **kwargs):
        super().__init__(**kwargs)
        self.buttons = None
        self.mainButton = None
        self.currentOption = 0
        self.open = False
        self.Arrow = None
        self.updateSelf(options)

    def updateSelf(self,options):
        self.Arrow = Image(source="Images/arrowRight.png")
        self.Arrow.size = (20,20)

        if self.buttons != None:
            for button in self.buttons:
                self.remove_widget(button)

        self.buttons = []

        i = -1
        for option in options:
            i += 1
            newButton = Button(text=option)
            newButton.size = self.size
            newButton.bind(on_press= lambda newbutton: (self.updateAnswer(newbutton,i)))
            newButton.background_color = (0.6,0.6,0.8,1)

            self.buttons.append(newButton)
            self.add_widget(newButton)




        if self.mainButton != None:
            self.remove_widget(self.mainButton)
        self.mainButton = Button(text="Select Option")
        self.mainButton.size = self.size
        self.mainButton.bind(on_press=self.openSelf)
        self.mainButton.background_color = (0.2,0.2,0.7,1)

        self.add_widget(self.mainButton)
        self.add_widget(self.Arrow)
    def openSelf(self,instance):
        self.open = not self.open
    def updateAnswer(self,button,index):
        whoami = -1
        for i in range(0,len(self.buttons)):
            if button == self.buttons[i]:
                whoami = i

        self.currentOption = whoami
        self.open = False
    def update(self):
        self.mainButton.text = self.buttons[self.currentOption].text
        self.mainButton.center = self.center
        self.Arrow.center = (self.center_x - 80, self.center_y)
        for index in range(len(self.buttons)):
            button = self.buttons[index]
            if self.open:
                button.disabled = False
                button.center = (self.center_x, self.center_y-(button.height * (index + 1)))
                self.Arrow.source = "Images/arrowDown.png"
            else:
                button.disabled = True
                button.center = self.center
                self.Arrow.source = "Images/arrowRight.png"


