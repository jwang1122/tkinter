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
        return self.cardX

    def getY(self):
        return self.cardY

    def __repr__(self) -> str:
        return self.name

class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"
        self.seat = "NORTH"
        self.hand = []
        self.cardX = self.seats[self.seat][0]
        self.cardY = self.seats[self.seat][1]

    def deal(self):
        print("Deal card")

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

    def deal(self):
        # print('Deal Card button is clicked...')
        self.dealer.deal()

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

    def displayPlayerNames(self):
        for player in self.playerList:
            Label(self.root, text=player.name, bg=self.bg).place(x=player.getX()-50, y=player.getY())

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