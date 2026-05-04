
from kivy.uix.widget import Widget


class basePage(Widget):
    def __init__(self,**kwargs):
        Widget.__init__(self,**kwargs)
        self.Parent = None
    def setup(self,parent):
        self.Parent =parent




        self.center = parent.center

    def updatePage(self):
        self.center = self.parent.center
