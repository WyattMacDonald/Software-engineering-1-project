from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from matplotlib.dviread import Page
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from customWidgets.Dropdown import Dropdown
from customWidgets.AnswerInstance import AnswerEditInstance
from customWidgets.ImageButton import ImageButton


class QuestionEdit(Widget):

    def __init__(self,**kwargs):
        Widget.__init__(self,**kwargs)
        self.whoAmI = -1
        self.inputedQuestion = None
        self.questionText = None
        self.questionInputs = None
        self.typeofQuestion = 0
        self.questionContainer = None

        self.addAnswerButton = None

        self.AnswerDropdown = None
        self.imageText = None
        self.writtenAnswer = None
        self.randomizedButton = None
        self.formatDropdown = None
        self.deleteQuestionButton = None
        self.imFilled = False
        self.RemoveMe = False
        self.turnRandomized = False
        self.questionLabel = None
        self.questionTextLabel = None
        self.randomizeLabel = None
        self.AddAnswerLabel = None
        self.formatLabel = None
        self.ImageLabel = None

    sizeX = NumericProperty(0)
    sizeY = NumericProperty(0)
    posX = NumericProperty(0)
    posY = NumericProperty(0)
    def updateProperties(self):
        self.sizeX = 700
        self.sizeY = 800
        self.posX = self.center_x
        self.posY = self.center_y

    def makeLetterList(self,count):
        letterList = []
        for i in range(count):
            letter = chr(ord('A') + i)
            letterList.append(""+letter)
        return letterList
    def updateSelf(self,whoami,inputedQuestion):
        self.whoAmI = whoami

        self.inputedQuestion = inputedQuestion
        self.typeofQuestion = inputedQuestion.formatType

        if (self.questionContainer != None):
            self.remove_widget(self.questionContainer)
        if self.questionInputs != None:
            for question in self.questionInputs:
                self.remove_widget(question)
        if self.addAnswerButton != None:
            self.remove_widget(self.addAnswerButton)
        if (self.questionText != None):
            self.remove_widget(self.questionText)
        if (self.writtenAnswer != None):
            self.remove_widget(self.writtenAnswer)
        if (self.formatDropdown != None):
            self.remove_widget(self.formatDropdown)
        if self.AnswerDropdown != None:
            self.remove_widget(self.AnswerDropdown)
        if self.deleteQuestionButton != None:
            self.remove_widget(self.deleteQuestionButton)
        if self.randomizedButton != None:
            self.remove_widget(self.randomizedButton)
        if self.imageText != None:
            self.remove_widget(self.imageText)
        if self.questionLabel != None:
            self.remove_widget(self.questionLabel)
        if self.questionTextLabel != None:
            self.remove_widget(self.questionTextLabel)
        if self.ImageLabel != None:
            self.remove_widget(self.ImageLabel)
        if self.AddAnswerLabel != None:
            self.remove_widget(self.AddAnswerLabel)
        if self.randomizeLabel != None:
            self.remove_widget(self.randomizeLabel)

        self.questionLabel = Label(text = "Question " + str(self.whoAmI+1) + ":")
        self.questionLabel.font_size = 35
        self.add_widget(self.questionLabel)

        self.imageText = TextInput(multiline=False,size = (200,60))
        self.add_widget(self.imageText)

        self.ImageLabel = Label(text = "Insert Image link here\n(leave blank for no image): ")
        self.add_widget(self.ImageLabel)



        self.questionText = TextInput(multiline=False)

        self.questionText.size = (500,200)
        self.add_widget(self.questionText)

        self.questionTextLabel = Label(text = "Enter your question here:")
        self.questionTextLabel.color = (0,0,0,1)
        self.add_widget(self.questionTextLabel)
        if (self.typeofQuestion == 0):
            self.multipleChoiceFormat(inputedQuestion)
        if (self.typeofQuestion == 1):
            self.writtenChoiceFormat(inputedQuestion)



        self.formatDropdown = Dropdown(["Multi Choice", "Written"], size=(200, 50))
        self.formatDropdown.center = (self.center_x, self.center_y)
        self.formatDropdown.currentOption = inputedQuestion.formatType
        self.add_widget(self.formatDropdown)

        self.formatLabel = Label(text = "Question Format")
        self.add_widget(self.formatLabel)


        if self.whoAmI != 0:
            self.deleteQuestionButton = Button(text="X")
            self.deleteQuestionButton.center = (self.center_x+self.sizeX/2, self.center_y+self.sizeY/2)
            self.deleteQuestionButton.bind(on_press=self.remove)
            self.add_widget(self.deleteQuestionButton)


    def remove(self,instance):
        self.RemoveMe = True

    def randomize(self,instance):
        self.turnRandomized = not self.turnRandomized

    def multipleChoiceFormat(self,inputedQuestion):
        self.questionContainer = GridLayout(cols=1, spacing=100, size_hint=(1, 1))

        self.randomizedButton = ImageButton("Images/selectionNonFilled.png",size = (40,40))
        self.randomizedButton.background_color = (0.2,0.2,0.2,0)
        self.randomizedButton.image.color = (0.2,0.2,0.2,1)
        self.randomizedButton.bind(on_press=self.randomize)
        self.randomizeLabel = Label(text = "Randomized Order:")



        self.add_widget(self.randomizedButton)
        self.add_widget(self.randomizeLabel)


        self.questionInputs = []
        for index in range(len(inputedQuestion.answers)):
            questionInput = AnswerEditInstance()
            questionInput.update(index)
            questionInput.answer.text = inputedQuestion.answers[index]
            self.questionInputs.append(questionInput)

            self.questionContainer.add_widget(questionInput)


        self.addAnswerButton = Button(text="+")
        self.addAnswerButton.size = (40, 40)
        self.addAnswerButton.bind(on_press=self.addAnswer)
        self.addAnswerButton.color = (1.0, 1, 1, 1)
        self.addAnswerButton.background_color = (0.1, 1, 1, 1)
        self.AddAnswerLabel = Label(text = "Add Answer:")
        self.add_widget(self.AddAnswerLabel)

        self.add_widget(self.addAnswerButton)
        self.add_widget(self.questionContainer)

        self.changeAnswerDropdown()



    def writtenChoiceFormat(self,inputedQuestion):
        self.writtenAnswer = TextInput(multiline=True)
        self.writtenAnswer.size = (500,300)
        self.writtenAnswer.center = (self.center_x, self.center_y + 250)
        self.add_widget(self.writtenAnswer)


    def changeAnswerDropdown(self,doupdate = False):
        if self.AnswerDropdown != None:
            self.remove_widget(self.AnswerDropdown)
        self.AnswerDropdown = Dropdown(self.makeLetterList(len(self.questionInputs)),size=(200,50))

        self.add_widget(self.AnswerDropdown)
        if doupdate:
            self.updateQuestion()



    def addAnswer(self,instance):
        NewAnswer = AnswerEditInstance()
        NewAnswer.update(len(self.questionInputs))
        print("touched")
        self.questionContainer.add_widget(NewAnswer)
        self.questionInputs.append(NewAnswer)

        self.updateQuestion()
        self.changeAnswerDropdown(True)

    def updateQuestion(self):

        questionFormat = self.inputedQuestion.formatType

        self.inputedQuestion.question_text = self.questionText.text
        self.inputedQuestion.image = self.imageText.text


        if questionFormat == 0:
            self.inputedQuestion.answers = []
            self.inputedQuestion.answer_index = self.AnswerDropdown.currentOption
            self.inputedQuestion.randomized = self.turnRandomized
            for index in range(0, len(self.questionInputs)):
                self.inputedQuestion.answers.append(self.questionInputs[index].answer.text)
        if questionFormat == 1:
            self.inputedQuestion.answers[0] = self.writtenAnswer.text

    def updateandCheckQuestions(self):
        self.updateProperties()

        questionFormat = self.inputedQuestion.formatType
        self.formatDropdown.center = (self.center_x+200, self.center_y-320)
        self.formatDropdown.update()

        self.formatLabel.center = (self.center_x+200, self.center_y-280)

        self.questionText.center = (self.center_x, self.center_y + 220)
        self.questionTextLabel.center = (self.center_x, self.center_y+350)
        self.imageText.center = (self.center_x-200, self.center_y - 340)
        self.ImageLabel.center = (self.center_x-200, self.center_y-280)
        self.questionLabel.center = (self.center_x-self.sizeX/2+100, self.center_y + self.sizeY/2-20)
        if self.deleteQuestionButton != None:
            self.deleteQuestionButton.center = (self.center_x+self.sizeX/2, self.center_y+self.sizeY/2)
        if (questionFormat == 0):
            self.addAnswerButton.center = (self.center_x + 300, self.center_y - 120)
            self.AddAnswerLabel.center = (self.center_x + 200, self.center_y - 120)
            self.questionContainer.center = (self.center_x - 130, self.center_y + 35)
            self.randomizedButton.center = (self.center_x + 300, self.center_y - 180)
            self.AnswerDropdown.center = (self.center_x + 200, self.center_y +40)
            self.AnswerDropdown.update()

            self.randomizeLabel.center = (self.center_x + 170, self.center_y - 180)

            if self.turnRandomized:
                self.randomizedButton.image.source = "Images/selectionFilled.png"
            else:
                self.randomizedButton.image.source = "Images/selectionNonFilled.png"

            for index in range(0, len(self.questionInputs)):
                self.questionInputs[index].arrange()
        if (questionFormat == 1):
            self.writtenAnswer.center = (self.center_x, self.center_y - 100)

        if questionFormat != self.formatDropdown.currentOption:
            self.inputedQuestion.set_format(self.formatDropdown.currentOption)
            self.updateSelf(self.whoAmI, self.inputedQuestion)

        removeList = []
        resetList = False
        for index in range(0, len(self.questionInputs)):
            question = self.questionInputs[index]
            if question.RemoveMe:
                removeList.append(index)
                resetList = True
        for index in removeList:
            self.questionInputs.pop(index)
        if resetList:
            self.updateQuestion()
            self.updateSelf(self.whoAmI, self.inputedQuestion)

    def checkIfFinished(self):
        if self.questionText.text == "":
            return False
        if self.typeofQuestion == 0:
            for q in self.questionInputs:
                if q.answer.text == "":
                    return False
        if self.typeofQuestion == 1:
            if self.writtenAnswer.text == "":
                return False


        return True
