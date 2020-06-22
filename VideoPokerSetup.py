from util.Cards import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from util.PokerHands import *
from requests import *
from PIL import Image
from io import BytesIO
from PyQt5 import QtCore
from util.Stack import Stack

class VP(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setWindowTitle("Video Poker")         #Set Window Title
        self.setGeometry(0,0,800,600)              #set size
        self.assignlabels()
        self.assignbuttons()
        self.turn=0
        self.layouts()
        self.startgame()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key()==QtCore.Qt.Key_Escape:       #if person hits escape, then quit
            self.close()
        if QKeyEvent.key()==QtCore.Qt.Key_Return:       #if hits enter, then cards are drawn
            self.change()

    def assignlabels(self): 
        self.title=QLabel(self)                        #set title
        self.title.setText("Video Poker")              #set text
        self.title.setAlignment(QtCore.Qt.AlignCenter) #align
        font=QFont()              #create font
        font.setPointSize(72)     #set size
        font.setFamily("Arial")   #set font
        self.title.setFont(font)  #assign
        self.title.adjustSize()   #make it fit 
        self.instructions=QLabel(self)                 #set instructions
        self.instructions.setText('''This version is jacks or better. Any hand greater than or equal to a pair of jacks will win. Press h for list of poker hands or p for payout chart.''')
        self.instructions.setAlignment(QtCore.Qt.AlignCenter)     
        self.instructions.adjustSize()
        self.layout=QHBoxLayout()
        self.labels=[]
        for i in range(5):                              #create labels for images of cards
            self.labels.append(QLabel())
        for i in self.labels:                           #add to box layout
            self.layout.addWidget(i)
    
    def assignbuttons(self):
        self.buttons=[]                                 #create checkboxes
        for i in range(5):
            self.buttons.append(QCheckBox("Change",self))      #label them
        self.horizontalbuttons= QHBoxLayout()
        for i in self.buttons:                          #add to box layout
           self.horizontalbuttons.addWidget(i)
        self.buttonenter=QPushButton(self)              #create button for drawing
        self.buttonenter.clicked.connect(self.change)
        self.buttonenter.setText("Draw")

    def layouts(self):
        vert=QVBoxLayout()                           #main vertical layout
        vert.addWidget(self.title)                   #add title
        vert.addWidget(self.instructions)            #add instructions
        vert.addLayout(self.layout)                  #add layout of cards
        vert.addLayout(self.horizontalbuttons)       #add layout of buttons
        vert.addSpacing(100)                         #add spacing
        vert.addWidget(self.buttonenter)             #add button
        vert.addSpacing(100)
        self.setLayout(vert)

    def startgame(self):
        self.turn +=1 
        self.cards=start()                           #get cards
        self.cards=randomize(self.cards)             #shuffle
        self.disposal=Stack()                        #create disposal deck for changed cards
        self.deal()

    def deal(self):
        self.hidden=[]
        for i in range(5):                           #get five cards
            self.hidden.append(self.cards.pop())
        c=0
        for i in self.labels:
            r=requests.get(self.hidden[c].url)       #get image of card
            image=Image.open(BytesIO(r.content))
            try:
                image.save("Temp1"+"."+image.format,image.format)     #save as temp
            except IOError:
                a=6
            image=Image.open("Temp1."+image.format)                   #open
            image=image.resize((80,100),Image.ANTIALIAS)              #resize tofit
            image.save("Temp1.png")
            self.pixmap=QPixmap("Temp1.png")                          #put on pixmap
            i.setPixmap(self.pixmap)                                  #put on screen
            c+=1
    
    def change(self):
        self.turn+=1
        for i in range(5):
            if self.buttons[i].isChecked()==True:                   #if button is checked
                self.dispose(self.hidden[i])                       #dispose card
                self.hidden[i]=self.cards.pop()                    #get new card
                r=requests.get(self.hidden[i].url)
                image=Image.open(BytesIO(r.content))               #get new image of card
                try:
                    image.save("Temp1"+"."+image.format,image.format)
                except IOError:
                    a=6
                image=Image.open("Temp1."+image.format)
                image=image.resize((80,100),Image.ANTIALIAS)
                image.save("Temp1.png")
                self.pixmap=QPixmap("Temp1.png")
                self.labels[i].setPixmap(self.pixmap)
                
        self.buttonenter.setDisabled(True)                        #disable change button
        self.determine()

    def dispose(self,card):
        self.disposal.push(card)                                #put into disposal deck changed cards

    def determine(self):
        temp=[]                                                 #get list of values of cards
        for i in self.hidden:
            temp.append(i.value)
        temp.sort(reverse=True)

        temp2=[]                                                #get list of suits
        for i in self.hidden:
            temp2.append(i.suit)
        j=findout(temp,temp2)                                   #get poker hand
        self.printresult(j,temp)                                #print result
        self.endturn()                                          #end turn
    
    def printresult(self,num,list):
        self.word=""
        options=["royalflush","straightflush", "four of a kind","full house","flush","straight","three of a kind", "two pair","pair","high card"]
        if options[num] != "pair" and options[num]!="high card":
            self.word="You won! You got a " +options[num]+"."            #tell result if greater than pair
            return True
        else:
            for i in list:              #prints how many occurrences of each item in list
                if list.count(i)>=2:    #if at least two there is a pair
                    if i >=11:
                        self.word="You won! You got a pair of jacks or better."      #tell person they had greater than jacks if they did
                        return True
            self.word="You lost. You got less than a pair of jacks."                 #if not, tells person they lost
            return False

    def endturn(self):
        results=QMessageBox()
        temp=results.question(self,"Result", self.word+ " Want to play again?", results.Yes | results.No)   #message box to continue or not
        if temp==results.Yes:          #if yes
            for i in self.hidden:           #dispose used cards
                self.disposal.push(i)
            self.cards=empty(self.disposal,self.cards)      #add disposal to main deck
            self.cards=randomize(self.cards)                #shuffle 
            self.buttonenter.setDisabled(False)             #enable button again to draw
            for i in self.buttons:                          #deselect any boxes the person changed last round
                if i.isChecked()==True:
                    i.setChecked(False)
            self.startgame()                                #start game again
            self.word=""
        elif temp==results.No:                              #if not quit
            self.close()


if __name__ == "__main__":
    import sys
    app=QApplication(sys.argv)
    f=VP()
    f.show()
    sys.exit(app.exec_())
