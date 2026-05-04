from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from matplotlib.dviread import Page
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from customWidgets.AnswerInstance import AnswerEditInstance

class ImageButton(Button):

    def __init__(self,ImagePath, **kwargs):
        super(ImageButton, self).__init__(**kwargs)

        self.ids.buttonImage.source = ImagePath

        self.image = self.ids.buttonImage


