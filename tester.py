#!/bin/env/python3

from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar, QWidget, QGridLayout, QGroupBox, QTabWidget, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QAbstractItemView, QVBoxLayout
from PyQt5.QtGui import QIcon, QKeySequence, QColor, QFont
from PyQt5.QtCore import Qt
from sys import argv,exit
from squirrel import ValueBase
from random import choice

# Create Words Database
words=ValueBase(
    ["Steam","Buhar"],
    ["Stick","Sopa"],
    ["Brick","Tuğla"],
    ["Translate","Çevir"],
    ["Boat","Bot"],
    ["House","Ev"],
    ["Home","Yuva"],
    ["Camel","Deve"],
    ["Print","Yazdır"],
    ["Bear","Ayı"],
    ["Beer","Bira"],
    ["Again","Yeniden"],
    ["Again","Tekrar"],
    ["Specie","Madeni para"]
)
# Create Quiz History
history=ValueBase()
unasked=words.clone()
    
# Create Main Window
class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin,self).__init__()
        
        # Set Window Properties
        self.setFixedSize(400,self.minimumHeight())
        self.setWindowTitle("Worder")
        self.show()
        
        # Set Central Widget
        self.central=Central()
        self.setCentralWidget(self.central)
        
        # Set Status Bar
        self.l_status=QStatusBar()
        self.setStatusBar(self.l_status)

# Create Central Widget
class Central(QWidget):
    def __init__(self):
        super(Central,self).__init__()
        
        # Set Layouts
        self.layout=QGridLayout(self)
        
        # Create Tab Widgets
        self.tList=ListTab()
        self.tQuiz=QuizTab()
        
        # Create Tab Widget
        self.tabs=QTabWidget(self)
        self.tabs.addTab(self.tQuiz,"Quiz")
        self.tabs.addTab(self.tList,"Word List")
        
        self.layout.addWidget(self.tabs)

# Create "Word Add" Tab
class ListTab(QWidget):
    def __init__(self):
        super(ListTab,self).__init__()
        
        # Set Layout
        self.layout=QVBoxLayout(self)
        
        # Create "Add Word" Widgets
        self.gAdd=QGroupBox("Add New Word",self)
        self.glAdd=QGridLayout(self.gAdd)
        
        self.tWords=QTableWidget(1,2,self)
        self.lEnglish=QLabel("English",self)
        self.lTurkish=QLabel("Turkish",self)
        self.eEnglish=QLineEdit(self)
        self.eTurkish=QLineEdit(self)
        self.bAdd=QPushButton("Add Word")
        
        self.glAdd.addWidget(self.lEnglish,0,0)
        self.glAdd.addWidget(self.lTurkish,0,1)
        self.glAdd.addWidget(self.eEnglish,1,0)
        self.glAdd.addWidget(self.eTurkish,1,1)
        self.glAdd.addWidget(self.bAdd,1,2)
        
        # Create "Search" Widgets
        self.gSearch=QGroupBox("Search",self)
        self.glSearch=QVBoxLayout(self.gSearch)
        
        self.eSearch=QLineEdit(self)
        
        self.glSearch.addWidget(self.eSearch)
        
        # Widget Settings
        self.tWords.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tWords.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tWords.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tWords.setEditTriggers(QTableWidget.NoEditTriggers)
        
        # Add Widgets to Layout
        self.layout.addWidget(self.gAdd)
        self.layout.addWidget(self.gSearch)
        self.layout.addWidget(self.tWords)
        
        # Connect Methods to Events
        self.bAdd.clicked.connect(self.addWord)
        self.eSearch.textChanged.connect(self.reloadTable)
        
        # Initialize methods
        self.reloadTable()
    
    # Define Word Add Method
    def addWord(self):
        # Get Words
        en=self.eEnglish.text().capitalize().strip()
        tr=self.eTurkish.text().capitalize().strip()
        # Check Word Is Not Already Exists 
        if "" not in [tr,en] and \
           not words.queries((en,tr),(True,True),(False,False),[[0],[1]]):
            words.add(en,tr)
        # Sord Data Base
        words.sort()
        # Reload Table
        self.reloadTable()
        
    # Define Table Reloader
    def reloadTable(self,qry=""):
        # Get Search Bar Text
        qry=self.eSearch.text()
        # Make Query By Search Bar
        data=words.query(qry)
        # Set Data In Table
        self.tWords.setRowCount(len(data))
        for row in range(len(data)):
            for cell in range(data.columnCount):
                self.tWords.setItem(row,cell,QTableWidgetItem(data[row][cell]))

# Create Quiz Tab
class QuizTab(QWidget):
    def __init__(self):
        super(QuizTab,self).__init__()
        # Set Layout
        self.layout=QVBoxLayout(self)

        # Create "Quiz Section" Widgets
        self.gQuiz=QGroupBox("Question",self)
        self.glQuiz=QGridLayout(self.gQuiz)
        
        self.lEnglish=QLabel("English",self)
        self.lTurkish=QLabel("Turkish",self)
        self.eEnglish=QLineEdit(self)
        self.eTurkish=QLineEdit(self)
        
        self.glQuiz.addWidget(self.lEnglish,0,0)
        self.glQuiz.addWidget(self.lTurkish,0,1)
        self.glQuiz.addWidget(self.eEnglish,1,0)
        self.glQuiz.addWidget(self.eTurkish,1,1)

        # Create "Answer Section" Widgets
        self.gAnswer=QGroupBox("Question",self)
        self.glAnswer=QGridLayout(self.gAnswer)
        self.lAnswer=QLabel("Correct Answer:",self)
        self.lCorrect=QLabel("None",self)
        
        self.bSubmit=QPushButton("Submit")
        self.bNext=QPushButton("Next Question",self.gAnswer)
        
        self.glAnswer.addWidget(self.lAnswer,0,0)
        self.glAnswer.addWidget(self.lCorrect,0,1)
        self.glAnswer.addWidget(self.bSubmit,1,0)
        self.glAnswer.addWidget(self.bNext,1,1)

        # Create "Quiz Progress" Widgets
        self.gProgress=QGroupBox("Progress",self)
        self.glProgress=QGridLayout(self.gProgress)
        
        self.lNumber=QLabel("Question",self)
        self.lvNumber=QLabel("0",self)
        self.lTrue=QLabel("True",self)
        self.lvTrue=QLabel("0",self)
        self.lFalse=QLabel("False",self)
        self.lvFalse=QLabel("0",self)
        self.lEmpty=QLabel("Empty",self)
        self.lvEmpty=QLabel("0",self)
        self.bFinish=QPushButton("Finish Quiz",self.gProgress)
        self.bRetake=QPushButton("Retake Quiz",self.gProgress)
        
        self.glProgress.addWidget(self.lNumber,0,0)
        self.glProgress.addWidget(self.lTrue,0,1)
        self.glProgress.addWidget(self.lFalse,0,2)
        self.glProgress.addWidget(self.lEmpty,0,3)
        self.glProgress.addWidget(self.lvNumber,1,0)
        self.glProgress.addWidget(self.lvTrue,1,1)
        self.glProgress.addWidget(self.lvFalse,1,2)
        self.glProgress.addWidget(self.lvEmpty,1,3)
        self.glProgress.addWidget(self.bFinish,2,0,1,2)
        self.glProgress.addWidget(self.bRetake,2,2,1,2)
        
        # Widget Settings
        self.lAnswer.setAlignment(Qt.AlignRight)
        self.lNumber.setAlignment(Qt.AlignCenter)
        self.lTrue.setAlignment(Qt.AlignCenter)
        self.lFalse.setAlignment(Qt.AlignCenter)
        self.lEmpty.setAlignment(Qt.AlignCenter)
        self.lvNumber.setAlignment(Qt.AlignCenter)
        self.lvTrue.setAlignment(Qt.AlignCenter)
        self.lvFalse.setAlignment(Qt.AlignCenter)
        self.lvEmpty.setAlignment(Qt.AlignCenter)
        
        # Add Widgets to Layout
        self.layout.addWidget(self.gQuiz)
        self.layout.addWidget(self.gAnswer)
        self.layout.addWidget(self.gProgress)
        
        # Connect Methods to Widgets
        self.bNext.clicked.connect(self.askQuestion)
        self.bSubmit.clicked.connect(self.checkAnswer)
        self.bFinish.clicked.connect(self.finishExam)
        self.bRetake.clicked.connect(self.retakeExam)
        
        # Set Variables
        self.answer=None
        self.askWhich=0
        self.toAsk=[]
        self.vNum=0
        self.vTrue=0
        self.vFalse=0
        self.vEmpty=0
        self.answered=False
        self.finished=False
        
        # Initialize Methods
        self.askQuestion()
        self.bRetake.setDisabled(True)
    
    # Define Question Asking Method
    def askQuestion(self):        
        # Clear Correct Answer
        self.lCorrect.setStyleSheet("color:unset")
        self.lCorrect.setText("?")
        # Check If There Is At Least One Word Unasked
        if unasked:
            # Clean Entries
            self.eEnglish.setDisabled(False)
            self.eTurkish.setDisabled(False)
            self.eEnglish.setText("")
            self.eTurkish.setText("")
            # Select What To Ask
            self.toAsk=choice(unasked)
            self.askWhich=choice([0,1])
            if self.askWhich==1:
                self.eEnglish.setText(self.toAsk[0])
                self.eEnglish.setDisabled(True)
                self.answer=self.toAsk[1]
                self.eTurkish.setFocus()
            else:
                self.eTurkish.setText(self.toAsk[1])
                self.eTurkish.setDisabled(True)
                self.answer=self.toAsk[0]
                self.eEnglish.setFocus()
            # Remove Asked Word From List
            unasked.removeRow(unasked.indexof(self.toAsk))
            # Increase Question Number
            self.vNum+=1
            self.lvNumber.setText(f"{self.vNum}/{len(words)}")
            # Set Answered False
            self.answered=False
            self.updateButtons()
        else:
            win.statusBar().showMessage("No unasked word left in word list.",2000)
        unasked.print()
    
    # Define Answer Checking Method
    def checkAnswer(self):
        # Get User Answer
        ans=self.eEnglish.text() if self.askWhich==0 else self.eTurkish.text()
        ans=ans.capitalize().strip()
        # Check and Increase Values
        if ans==self.toAsk[self.askWhich]:
            self.vTrue+=1
            self.lvTrue.setText(str(self.vTrue))
            self.lCorrect.setStyleSheet("color:green")
        elif ans=="":
            self.lCorrect.setStyleSheet("color:tomato")
            self.vEmpty+=1
            self.lvEmpty.setText(str(self.vEmpty))
        else:
            self.lCorrect.setStyleSheet("color:red")
            self.vFalse+=1
            self.lvFalse.setText(str(self.vFalse))
        # Write Correct Answer
        self.lCorrect.setText(self.toAsk[self.askWhich])
        # Register Answer To History
        history.add(*self.toAsk,self.askWhich,ans)
        # Set Answered True
        self.answered=True
        self.updateButtons()
        self.bNext.setFocus()
        
    # Define Button Disabler
    def updateButtons(self):
        print(self.answered)
        self.bSubmit.setDisabled(self.answered)
        self.bNext.setDisabled(not self.answered if unasked else True)
        
    # Define Finish Exam Method
    def finishExam(self):
        history.print()
        self.finished=True
        self.updateRetakable()
        
    # Define Update Retakable Button
    def updateRetakable(self):
        self.bFinish.setDisabled(self.finished)
        self.bRetake.setDisabled(not self.finished)
        
    def retakeExam(self):
        # Recreate Unasked Words
        global unasked
        unasked=words.clone()
        
        # Set Variables
        self.answer=None
        self.askWhich=0
        self.toAsk=[]
        self.vNum=0
        self.vTrue=0
        self.vFalse=0
        self.vEmpty=0
        self.answered=False
        
        # Update Fields
        self.lvEmpty.setText("0")
        self.lvTrue.setText("0")
        self.lvFalse.setText("0")
        self.lvNumber.setText(f"1/{len(words)}")
        
        # Start Exam
        self.finished=False
        self.updateRetakable()
        self.askQuestion()

app=QApplication(argv)
win=MainWin()

exit(app.exec_())