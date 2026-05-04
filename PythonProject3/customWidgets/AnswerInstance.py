from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from matplotlib.dviread import Page
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label




class AnswerEditInstance(Widget):

    def __init__(self, **kwargs):
        super(AnswerEditInstance, self).__init__(**kwargs)
        self.whoAmI = -1

        self.answer = None

        self.label = None

        self.killbutton = None

        self.RemoveMe = False

        self.dontDolabel = False


    def arrange(self):
        self.label.center = (self.center_x - 180, self.center_y)
        self.answer.center = self.center
        if self.killbutton != None:
            self.killbutton.center = (self.center_x + 180, self.center_y)

    def update(self, whoAmI):
        self.whoAmI = whoAmI
        if not self.dontDolabel:
            if (self.label != None):
                self.remove_widget(self.label)

            character = chr(ord('A') + whoAmI)
            self.label = Label(text=character + ". ")
            self.label.color = (0, 0, 0.1, 1)
            self.label.center = (self.center_x - 300, self.center_y)
            self.add_widget(self.label)
        savedAnswer = ""
        if (self.answer != None):
            savedAnswer = self.answer.text
            self.remove_widget(self.answer)

        self.answer = TextInput(text=savedAnswer,multiline=False)
        self.answer.top = self.top
        self.answer.width = 300
        self.answer.height = 50

        if self.whoAmI != 0:
            if self.killbutton != None:
                self.remove_widget(self.killbutton)
            from customWidgets.ImageButton import ImageButton
            self.killbutton =  ImageButton("Images/trash.png")
            self.killbutton.image.color = (0, 0, 0.1, 1)
            self.killbutton.background_color = (1, 1, 1, 0)
            self.killbutton.bind(on_press=self.remove)
            self.killbutton.center = (self.center_x + 200, self.center_y)
            self.killbutton.size = (30,30)
            self.add_widget(self.killbutton)





        self.add_widget(self.answer)


    def remove(self,instance):
        self.RemoveMe = True


