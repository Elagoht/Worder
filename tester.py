#!/bin/env/python3

from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar, QWidget, QGridLayout, QGroupBox, QTabWidget, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QAbstractItemView, QVBoxLayout, QHBoxLayout, QDialog, QPlainTextEdit, QMessageBox, QCheckBox, QSpinBox
from PyQt5.QtGui import QIcon, QKeySequence, QColor, QFont
from PyQt5.QtCore import Qt
from sys import argv,exit
from squirrel import ValueBase
from random import choice, shuffle
from re import sub

# Create Words Database
words=ValueBase(
    ["Stem"," Kök, Gövde"],
    ["Dyslexic","Disleksi, Disleksik"],
    ["Reputation","Ün, İtibar, Şöhret"],
    ["Digest","Sindirim, Sindirmek"],
    ["Mend","Tamir"],
    ["Harsh","Ağır, Sert"],
    ["Marsh","Bataklık"],
    ["Creed","İnanç, Mezhep"],
    ["Greed","Açgözlülük"],
    ["Cruel","Acımasız"],
    ["Freak","Çatlak"],
    ["Forte","Kale, Güçlü Yön"],
    ["Fleet","Donanma"],
    ["Pout","Surat Asmak"],
    ["Dodgy","Tehlikeli, Şüpheli, Riskli"],
    ["Cage","Kafes"],
    ["Bound","Ciltli, Bağlı, Zorunlu"],
    ["Curl","Kıvrılmak"],
    ["Worship","Tapmak"],
    ["Treat","Tedavi Etmek"],
    ["Ferne","Eğrelti Otu"],
    ["Nerve","Sinir"],
    ["Boar","Domuz"],
    ["Crept","Süründü"],
    ["Smote","Etkilemek, Tutulmak"],
    ["Probe","İncelemek, Bulmak"],
    ["Yarn","İplik"],
    ["Croak","Vıraklamak"],
    ["Heave, Lift","Kaldırmak"],
    ["Limb","Uzuv"],
    ["Testament, Will","Vasiyet"],
    ["Defiant","Meydan Okuyan"],
    ["Defy","Meydan Okumak"],
    ["Labour","Emek"],
    ["Emmet, Ant","Karınca"],
    ["Sacrifice","Kurban Etmek"],
    ["Fleet","Filo, Donanma"],
    ["Sheer","Saf, Arı"],
    ["Breez","Esinti"],
    ["Breeze","Meltem"],
    ["Ripple","Dalgalanma"],
    ["Struggle","Mücadele Etmek"],
    ["Hange","Asmak"],
    ["Reunion","Kavuşmak"],
    ["Surrection","Sermaye"],
    ["Resurrection","Kıyamet, Yeniden Dirilme"],
    ["Cluster","Küme"],
    ["Vanish","Yok Olmak"],
    ["Divine","İlahi"],
    ["Wig","Peruk"],
    ["Vagabond","Serseri"],
    ["Do You Mind","Sakıncası Var Mı"],
    ["Gambler","Kumarbaz"],
    ["Apostle","Havari"],
    ["Caterpillar","Tırtıl"],
    ["Courage","Cesaret"],
    ["Invest","Yatırmak"],
    ["Intent","Niyet Amaç"],
    ["Secretive","Ketum"],
    ["Conjure","Çağrı"],
    ["Audit","Denetim"],
    ["Pendulum","Sarkaç"],
    ["Stare","Bakmak"],
    ["Glance","Bakış Atmak"],
    ["Embellish","Renk Katmak, Güzelleştirmek"],
    ["Braces","Diş Teli"],
    ["Clutch","El Çantası"],
    ["Sublime","Yüce"],
    ["Slack","Geniş, Gevşek, Bol"],
    ["Slacks","Bol Pantolon"],
    ["Shook","Salladı"],
    ["Dogma","Dogma"],
    ["Nonetheless","Her Şeye Rağmen"],
    ["Iron Out","Gidermek"],
    ["Significance","Önem"],
    ["Assumption","Varsayım"],
    ["Assume","Farz Etmek"],
    ["Egocentric","Benmerkezci"],
    ["Eager","İstekli"],
    ["Redundant, Unnecessary","Gereksiz"],
    ["Representative","Temsilci"],
    ["Ample","Bol"],
    ["Peer","Akran, Yaşıt"],
    ["Equate","Kıyaslanmak"],
    ["Crucial","Hayati"],
    ["Syllabus","Müfredat"],
    ["Lexical","Sözcüksel"],
    ["Desire","Arzulamak"],
    ["Clue","Ipucu"],
    ["Exposure","Maruz Kalma"],
    ["Plenty","Bolca"],
    ["Suggestopedia, Suggest","Öneri"],
    ["Tendency","Eğilim"],
    ["Approach","Yaklaşım, Yaklaşmak"],
    ["Deficiency","Eksiklik"],
    ["Noble","Soylu"],
    ["Emerge","Ortaya Çıkmak"],
    ["Conduct","Yürütmek"],
    ["Manner","Tavır"],
    ["Pertain","İlgili Olmak"],
    ["Stipulate","Öngörmek"],
    ["Compulsory","Zorunlu"],
    ["Compulse, Drug","Uyuşturucu"],
    ["Appendix","Dosya Eki"],
    ["Apparent","Görünen"],
    ["Apparently","Görünüşe Göre"],
    ["Despite","Aksine"],
    ["Concluded","Sonuçlandırılmış"],
    ["Assessment","Değerlendirme"],
    ["Convince","İkna Etmek"],
    ["Bargain","Pazarlık, Pazarlık Etmek"],
    ["Inevitably","Kaçınılmaz Olarak"],
    ["Concrete","Somut"],
    ["Acquisition, Win","Kazanmak"],
    ["Attentively","Dikkatle"],
    ["Rely","Güvenmek"],
    ["Settle","Yerleşmek"],
    ["Deputies","Milletvekilleri"],
    ["Cope","Başa Çıkmak"],
    ["Hole Punching","Delilik"],
    ["Faciliate","Kolaylaştırmak"],
    ["Withdrawal","Para Çekme"],
    ["Interchangeably","Birbirinin Yerine "],
    ["Subsequent","Sonraki"],
    ["Submersion","Daldırma"],
    ["Receptively","Çabukça Kavrayarak"],
    ["Practitioner","Uygulayıcı"],
    ["Scaffold","İskele"],
    ["Intonation","Tonlama"],
    ["Rehersal","Prova, Tekrarlamak"],
    ["Will","İrade, Vasiyet"],
    ["Tag","Künye"],
    ["Proper","Düzgün"],
    ["Regard","Saygınlık, Saygı"],
    ["Superstition","Batıl Inanç"],
    ["Low Key","Şatafatsız"],
    ["Stimuly","Uyarıcı"],
    ["Stalactite","Sarkıt"],
    ["Stalagmite","Dikit"],
    ["Restraint","Kısıtlama"],
    ["Stove","Soba"],
    ["Contemplate","Düşünmek"],
    ["Gaze","Bakış"],
    ["Stipend, Salary","Maaş"],
    ["Gibraltar","Cebelitarık"],
    ["Courtesy","Nezaket"],
    ["Attractive","Cazip"],
    ["Entrepreneur","Girişimci"],
    ["Consequence","Sonuç"],
    ["Chairman","Başkan"],
    ["Imperative","Zorunlu"],
    ["Export","İhraç"],
    ["Import","İthal"],
    ["Occasionally","Arada, Ara sıra"],
    ["Rural","Kırsal"],
    ["Dormitory","Yurt, Yatakhane, Koğuş"],
    ["Suffer","Acı Çekmek"],
    ["Assignment","Tez, Ödev"],
    ["Attend","Katılmak"],
    ["Specie","Madeni Para"],
    ["Magnificent, Wonderful, Gorgeous, Glorious","Muhteşem"],
    ["Exhibition","Sergilemek"],
    ["Enthusiasm","Heves"],
    ["Extinction","Tükenme"],
    ["Establish","Kurmak"],
    ["Precaution","Tedbir"],
    ["Branch","Şube, Dal, Kol"],
    ["Occurrences","Olay"]
)
# Create Quiz History
history=ValueBase()
unasked=words.clone()

# Create Practice History
practice=words.clone()

# Define Practice Shuffle Function
def shufflePractice(): 
    shuffle(practice._cells)

    
# Create Main Window
class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin,self).__init__()
        
        # Set Window Properties
        self.setMinimumSize(400,self.minimumHeight())
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
        self.tPractice=PracticeTab()
        
        # Create Tab Widget
        self.tabs=QTabWidget(self)
        self.tabs.addTab(self.tQuiz,"Quiz")
        self.tabs.addTab(self.tPractice,"Practice")
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
        self.bAdd=QPushButton("&Add Word")
        
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
        en=sub(r"\bi","İ",self.eEnglish.text().strip()).title()
        tr=sub(r"\bi","İ",self.eTurkish.text().strip()).title()
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
        self.lvAnswer=QLabel("Correct Answer:",self)
        self.lCorrect=QLabel("None",self)
        
        self.bSubmit=QPushButton("&Submit")
        self.bNext=QPushButton("Next &Question",self.gAnswer)
        
        self.glAnswer.addWidget(self.lvAnswer,0,0)
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
        self.bFinish=QPushButton("&Finish Quiz",self.gProgress)
        self.bRetake=QPushButton("&Retake Quiz",self.gProgress)
        
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
        self.lvAnswer.setAlignment(Qt.AlignRight|Qt.AlignCenter)
        self.lvAnswer.setWordWrap(True)
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
        # Check If Quiz Not Finished
        if self.finished: return
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
    
    # Define Correction Checker Method
    def checkCorrection(self,wanted:str,answer:str):
        # Get Words in Wanted and Answer
        answer=[sub(r"\bi","İ",word.strip()).title() for word in answer.split(",")]
        wanted=[sub(r"\bi","İ",word.strip()).title() for word in wanted.split(",")]
        return any(word in answer for word in wanted)
    
    # Define Answer Checking Method
    def checkAnswer(self):
        # Get User Answer
        ans=self.eEnglish.text() if self.askWhich==0 else self.eTurkish.text()
        # Check and Increase Values
        if ans.strip()=="":
            self.lCorrect.setStyleSheet("color:tomato")
            self.vEmpty+=1
            self.lvEmpty.setText(str(self.vEmpty))
        elif self.checkCorrection(self.toAsk[self.askWhich],ans):
            self.vTrue+=1
            self.lvTrue.setText(str(self.vTrue))
            self.lCorrect.setStyleSheet("color:green")
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
        self.bSubmit.setDisabled(self.answered)
        self.bNext.setDisabled(not self.answered if unasked else True)
    
    # Define Generate Result Log Method
    def generateLog(self):
        log=""
        for num, question in enumerate(history):
            given=question[1-question[2]]
            wanted=question[question[2]]
            answer=question[3]
            log+=f"""Question {num+1}:
  Given  : {given}
  Wanted : {wanted}
  Answer : {answer} ({"True" if self.checkCorrection(answer,wanted) else "False" if answer!="" else "Empty"})
"""
        return log
 
    # Define Finish Exam Method
    def finishExam(self):
        if QMessageBox.warning(self,"Finish Exam",f"Are you sure you want to finish exam? The results will be evaluate over {self.vNum} questions.",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)==QMessageBox.Yes:
            self.finished=True
            self.updateRetakable()
            res.show()
            res.log.setPlainText(self.generateLog())
        
    # Define Update Retakable Button
    def updateRetakable(self):
        self.bFinish.setDisabled(self.finished)
        self.bRetake.setDisabled(not self.finished)
        
    def retakeExam(self):
        # Recreate Unasked Words
        global unasked
        unasked=words.clone()
        history.truncate()
        
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

# Create Practice Tab
class PracticeTab(QWidget):
    def __init__(self):
        super(PracticeTab,self).__init__()
        # Set Layout
        self.layout=QGridLayout(self)
        
        # Set Variables
        self.counter=0

        # Create "Controls" Widgets
        self.gControls=QGroupBox("Controls",self)
        self.glControls=QHBoxLayout(self.gControls)
        
        self.bPrev=QPushButton("<",self.gControls)
        self.sCounter=QSpinBox(self.gControls)
        self.lNumber=QLabel(f"/ {len(practice)}",self.gControls)
        self.bNext=QPushButton(">",self.gControls)
        
        self.glControls.addWidget(self.bPrev)
        self.glControls.addWidget(self.sCounter)
        self.glControls.addWidget(self.lNumber)
        self.glControls.addWidget(self.bNext)
        
        # Create "English" Widgets
        self.gEnglish=QGroupBox("English",self)
        self.glEnglish=QHBoxLayout(self.gEnglish)
        
        self.lvEnglish=QLabel("",self.gEnglish)
        self.glEnglish.addWidget(self.lvEnglish)
        
        # Create "Turkish" Widgets
        self.gTurkish=QGroupBox("Turkish",self)
        self.glTurkish=QHBoxLayout(self.gTurkish)
        
        self.lvTurkish=QLabel("",self.gEnglish)
        self.glTurkish.addWidget(self.lvTurkish)
        
        # Create "Restart" Widgets
        self.gRestart=QGroupBox("Restart",self)
        self.glRestart=QVBoxLayout(self.gRestart)
        
        self.cShuffle=QCheckBox("Shuffle (Don't Keep Order)",self.gRestart)
        self.bRestart=QPushButton("Restart",self.gRestart)
        
        self.glRestart.addWidget(self.cShuffle)
        self.glRestart.addWidget(self.bRestart)
        
        # Add Widgets to Layout
        self.layout.addWidget(self.gControls,0,0,1,2)
        self.layout.addWidget(self.gEnglish,1,0,1,1)
        self.layout.addWidget(self.gTurkish,1,1,1,1)
        self.layout.addWidget(self.gRestart,2,0,1,2)
        
        # Widget Settings
        self.lvEnglish.setAlignment(Qt.AlignCenter)
        self.lvEnglish.setWordWrap(True)
        self.lvTurkish.setAlignment(Qt.AlignCenter)
        self.lvTurkish.setWordWrap(True)
        self.sCounter.setRange(1,len(practice))
        
        # Connect Methods To Widgets
        self.bRestart.clicked.connect(self.firstWord)
        self.bPrev.clicked.connect(self.prevWord)
        self.bNext.clicked.connect(self.nextWord)
        self.sCounter.valueChanged.connect(self.scrollWord)
        
        # Initialize Methods
        shufflePractice()
        self.showWord()
       
    # Define Show Word Method
    def showWord(self):
        self.lvEnglish.setText(practice[self.counter][0])
        self.lvTurkish.setText(practice[self.counter][1])
        self.sCounter.setValue(self.counter+1)
        
    # Define Previous Word Method
    def prevWord(self):
        if self.counter>0: self.counter-=1
        else: self.counter=len(practice)-1
        self.showWord()
    
    # Define Next Word Method
    def nextWord(self):
        if self.counter<len(practice)-1: self.counter+=1
        else: self.counter=0
        self.showWord()
        
    # Define Go Begining Method
    def firstWord(self):
        if self.cShuffle.isChecked():
            shufflePractice()
            self.cShuffle.setChecked(False)
        self.counter=0
        self.showWord()
        
    # Define Scroll Setter Method
    def scrollWord(self):
        self.counter=self.sCounter.value()-1
        self.showWord()

# Create Results Window
class Results(QDialog):
    def __init__(self):
        super(Results,self).__init__()
        # Set Window Settings
        self.setWindowTitle("Quiz Results")
        self.setFixedSize(400,500)
        self.setWindowModality(Qt.ApplicationModal)
        # Set Layout
        self.layout=QVBoxLayout(self)
        
        # Set Widgets
        self.log=QPlainTextEdit()
        
        # Widget Settings
        self.log.setReadOnly(True)
        self.log.setFont(QFont("monospace"))
        self.log.setContextMenuPolicy(Qt.NoContextMenu)
        
        # Place Widgets To Layout
        self.layout.addWidget(self.log)
        
app=QApplication(argv)
res=Results()
win=MainWin()

exit(app.exec_())
