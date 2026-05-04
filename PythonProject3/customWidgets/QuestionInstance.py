import time

from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from customWidgets.AnswerInstance import AnswerEditInstance
from customWidgets.QuizAnswerMulti import QuizAnswerMulti
from kivy.uix.gridlayout import GridLayout

import random


class questionInstance(Widget):
    def __init__(self, **kwargs):
        super(questionInstance, self).__init__(**kwargs)
        self.answers = None
        self.questionText = None
        self.textAnswer = None
        self.AnswerHolder = None

        self.answered = False
        self.insertedQuestion = None
        self.whoami = -1
        self.type = -1
        self.image = None

    def setup(self, index,inputedQuestion):

        self.whoami = index
        self.type = inputedQuestion.formatType
        self.insertedQuestion = inputedQuestion

        if self.insertedQuestion.image != "":
            realInput = ""
            for char in inputedQuestion.image:
                if ord(char) != 92:
                    realInput += char
                else:
                    realInput += '/'
            self.image = Image(source=realInput,size = (300,300))
            self.add_widget(self.image)



        if self.answers != None:
            for answer in self.answers:
                self.remove_widget(answer)
            answer = None
        if self.questionText != None:
            self.remove_widget(self.questionText)
        if self.textAnswer != None:
            self.remove_widget(self.textAnswer)
        if self.AnswerHolder != None:
            self.remove_widget(self.AnswerHolder)

        self.questionText = Label(text=inputedQuestion.question_text)
        self.questionText.halign = 'left'
        self.questionText.valign = 'top'
        self.questionText.text_size = (600,500)
        self.questionText.font_size = 40
        self.questionText.color = (1,1,1,1)
        self.add_widget(self.questionText)


        if self.type == 0:
            self.multiInput()
        if self.type == 1:
            self.textAnswer = TextInput(multiline=False)
            self.add_widget(self.textAnswer)


    def multiInput(self):
        self.AnswerHolder = GridLayout(cols = 1, spacing = 100)
        self.answers = []
        i = 0
        for question in self.insertedQuestion.answers:
            newanswer = QuizAnswerMulti()
            newanswer.setup(i,i,question)
            self.answers.append(newanswer)
            if not self.insertedQuestion.randomized:
                self.AnswerHolder.add_widget(newanswer)
            i += 1
        if self.insertedQuestion.randomized:
            random.seed(time.time())
            random.shuffle(self.answers)
            self.answers = self.answers
            for index in range(len(self.answers)):
                self.answers[index].index = index
                self.answers[index].setup(index,self.answers[index].RepersentedAnswer,self.answers[index].savedAnswer)
                self.AnswerHolder.add_widget(self.answers[index])
        self.add_widget(self.AnswerHolder)

    sizeX = NumericProperty(0)
    sizeY = NumericProperty(0)
    posX = NumericProperty(0)
    posY = NumericProperty(0)

    def updateProperties(self):
        self.sizeX = 700
        self.sizeY = 800
        self.posX = self.center_x
        self.posY = self.center_y

    def update(self):
        self.updateProperties()
        if self.image != None:
            self.image.center = (self.center_x + self.sizeX / 2 - 200, self.center_y + self.sizeY / 2 - 200)
        if self.answers != None:

            lowestIndex = -1
            lowestTime = 100000000

            for answer in self.answers:
                answer.update()
                if answer.selected:
                    if answer.timer < lowestTime:
                        lowestTime = answer.timer
                        if lowestIndex != -1:
                            self.answers[lowestIndex].selected = False
                        lowestIndex = answer.index
                    if answer.timer > lowestTime:
                        answer.selected = False

            self.AnswerHolder.center = (self.center_x, self.center_y)
        if self.textAnswer != None:
            self.textAnswer.center = (self.center_x, self.center_y-100)

        self.questionText.center = (self.center_x, self.center_y+100)

    def amIcorrect(self):
        self.update()
        if self.type == 0:
            for answer in self.answers:
                if answer.selected:
                    if answer.RepersentedAnswer == self.insertedQuestion.answer_index:
                        return True
                    else:
                        return False

        if self.type == 1:
            if self.textAnswer.text == self.insertedQuestion.answers[0]:
                return True
            else:
                return False
        return False