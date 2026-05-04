
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView

from customWidgets.ImageButton import ImageButton
from pages.CreateQuiz import createQuiz
from pages.QuizTaking import quizTaking
from pages.pageBase import basePage
from pages.homepage import HomePage


class appManager(Widget):
   currentPage = None
   hasStarted = False

   Quizzes = []
   currentQuizindex = -1
   homebutton = None

   def startup(self):
        home = HomePage()


        home.setup(self)
        self.homebutton = ImageButton("Images/house.png")
        self.homebutton.image.center_y = 100
        self.homebutton.background_color = ((111/255)*2.5,(189/255)*2.5,(249/255)*2.5,1)
        self.homebutton.bind(on_press=self.gohome)
        self.homebutton.center = (self.center_x-self.width/2+80, self.center_y+self.height/2-80)
        self.add_widget(self.homebutton)

        self.add_widget(home)
        self.currentPage = home
   def gohome(self,instance):
        self.switchPage(0)
   def update(self, dt):
       if not self.hasStarted:
           self.startup()
           self.hasStarted = True
       if self.currentPage is not None:
           self.currentPage.updatePage()
   def switchPage(self, page):

       if (page == 0):
           self.remove_widget(self.currentPage)
           newone = HomePage()
           newone.setup(self)
           self.currentPage = newone
           self.add_widget(newone)
       if (page == 1):
           self.remove_widget(self.currentPage)
           newone = createQuiz()
           newone.setup(self)
           self.currentPage = newone
           self.add_widget(newone)
       if (page == 2):
           self.remove_widget(self.currentPage)
           newone = quizTaking(center = self.center)
           newone.setup(self)
           print("worked")
           print(newone.testText())
           self.currentPage = newone
           self.add_widget(newone)





class quizCreatorApp(App):
    def build(self):

        self.window = appManager()
        self.window.scroll_distance = 10000000

        Clock.schedule_interval(self.window.update, 1.0 / 60.0)



        return self.window

if __name__ == '__main__':
    quizCreatorApp().run()