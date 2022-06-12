from tkinterbase import *
from PIL import ImageTk
import random

class Player:
    seats = {'WEST':(70, 300),'NORTH':(300, 30),'SOUTH':(300, 500), 'EAST':(650, 300)}
    def __init__(self, name, seat='EAST'):
        self.name = name
        self.seat = seat
        self.winCount = 0
        self.seat = seat
        self.hand = []
        self.cardX = self.seats[seat][0]
        self.cardY = self.seats[seat][1]

    def getX(self):
        self.cardX += 30
        return self.cardX

    def getY(self):
        return self.cardY

    def __repr__(self) -> str:
        return f'{self.name}: {self.hand}'

    def addCardToHand(self, card, frame):
        self.hand.append(card)
        img = card.getImage()
        label = Label(frame)
        card.setLabel(label)
        label.configure(image=img)
        label.image = img
        label.place(x=self.getX(), y=self.getY())
        if self.name=='Dealer' and len(self.hand)==2: #dealer has 2 card in hand
            filename = "images/backR.gif"
            img = ImageTk.PhotoImage(file=filename)
            self.facedown = Label(frame)
            self.facedown.configure(image=img)
            self.facedown.image = img
            self.facedown.place(x=self.cardX, y=self.getCardY())

class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"
        self.seat = "NORTH"
        self.deck = Deck()
        self.deck.shuffle()
        self.hand = []
        self.cardX = self.seats[self.seat][0]
        self.cardY = self.seats[self.seat][1]

    def deal(self):
        return self.deck.nextCard()

class Deck:
    suits = ["spade","club","diamond","heart"]
    faces = ["A",'2','3','4','5','6','7','8','9','10','J',"Q",'K']

    def __init__(self):
        self.cards = [Card(face, suit) for face in self.faces for suit in self.suits]
        self.currentIndex = 52

    def nextCard(self):
        self.currentIndex -= 1
        if self.currentIndex < 0:
            self.currentIndex = 51
        return self.cards[self.currentIndex]

    def shuffle(self):
        random.shuffle(self.cards)

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
    
    def __repr__(self):
        return '('+self.face+', '+self.suit+')'
    
    def getImage(self):
        filename = "images/"+self.suit+self.face+".gif"
        image = ImageTk.PhotoImage(file=filename)
        return image
    
    def getValue(self):
        if self.face.isdigit():
            return int(self.face)
        if self.face == 'A':
            return 11
        return 10

    def setLabel(self, label):
        self.label = label
    
    def getLabel(self):
        return self.label

class PlayBoard(TkinterBase):
    def buildWidget(self):
        self.dealer = Dealer()
        self.root.title("Blackjack Game")
        self.bg = '#568568'
        self.buildControlFrame()
        self.buildBoardFrame()
        self.buildResultFrame()
        self.index = -1

    def deal(self):
        # print('Deal Card button is clicked...')
        player = self.getCurrentPlayer()
        player.addCardToHand(self.dealer.deal(), self.root)
        print(player)

    def getCurrentPlayer(self):
        self.index += 1
        if self.index == 4:
            self.index = 0
        return self.playerList[self.index]
        
    def buildControlFrame(self):
        self.root.configure(bg=self.bg)
        self.playerName = StringVar()
        self.playerName.set("Dealer")
        ctrl = Frame(self.root, bg=self.bg)
        dealBtn = Button(ctrl, text="Deal Card", command=self.deal)
        dealBtn.pack(side=LEFT, padx=3)
        Button(ctrl, text="Result").pack(side=LEFT, padx=3)
        Button(ctrl, text="Configure").pack(side=LEFT, padx=3)
        Label(ctrl, text=" ", bg=self.bg).pack(side=LEFT, padx=300)
        Label(ctrl, text="Player: ", bg=self.bg).pack(side=LEFT, padx=5)
        Label(ctrl, textvariable=self.playerName, bg=self.bg).pack(side=LEFT, padx=5)
        Button(ctrl, text="Hit").pack(side=LEFT, padx=3)
        Button(ctrl, text="Pass").pack(side=LEFT, padx=3)
        ctrl.pack()

    def buildBoardFrame(self):
        self.buildPlayerList()
        self.displayPlayerNames()

    def buildResultFrame(self):
        westValue = StringVar()
        westValue.set(0)
        resultFrame = LabelFrame(self.root, text="Game Result", bg='yellow')
        Label(resultFrame, text="East", bg='yellow').grid(row=1, column=1)
        Label(resultFrame, textvariable=westValue, bg='yellow').grid(row=1, column=2)
        Label(resultFrame, text="South", bg='yellow').grid(row=2, column=1)
        Label(resultFrame, textvariable=westValue, bg='yellow').grid(row=2, column=2)
        Label(resultFrame, text="West", bg='yellow').grid(row=3, column=1)
        Label(resultFrame, textvariable=westValue, bg='yellow').grid(row=3, column=2)
        Label(resultFrame, text="Dealer", bg='yellow').grid(row=4, column=1)
        Label(resultFrame, textvariable=westValue, bg='yellow').grid(row=4, column=2)
        resultFrame.place(x=900, y=50)

    def displayPlayerNames(self):
        for player in self.playerList:
            Label(self.root, text=player.name, bg=self.bg).place(x=player.getX()-20, y=player.getY())

    def buildPlayerList(self):
        self.playerList = []
        player = Player("East", "EAST")
        self.playerList.append(player)
        player = Player("South", "SOUTH")
        self.playerList.append(player)
        player = Player("West", "WEST")
        self.playerList.append(player)
        player = Player("Dealer", "NORTH")
        self.playerList.append(player)
        

if __name__ == '__main__':
    PlayBoard()