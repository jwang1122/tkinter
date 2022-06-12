"""
blackjack card game gui
"""
import tkinter as tk
from PIL import Image, ImageTk
import random
from tkinterbase import *

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

class Player:
    seats = {'W':(70, 300),'N':(300, 30),'S':(300, 500), 'E':(800, 300)}
    def __init__(self, name, seat='W'):
        self.name = name
        self.winCount = 0
        self.seat = seat
        self.hand = []
        self.cardX = self.seats[seat][0]
        self.cardY = self.seats[seat][1]

    def win(self):
        self.winCount += 1

    def __repr__(self):
        return self.name

    def getCardX(self):
        self.cardX += 30
        return self.cardX
    
    def getCardY(self):
        return self.cardY

    def addCardToHand(self, card, frame):
        self.hand.append(card)
        img = card.getImage()
        label = tk.Label(frame)
        card.setLabel(label)
        label.configure(image=img)
        label.image = img
        label.place(x=self.getCardX(), y=self.getCardY())
        if self.name=='Dealer' and len(self.hand)==2: #dealer has 2 card in hand
            filename = "images/backR.gif"
            img = ImageTk.PhotoImage(file=filename)
            self.facedown = tk.Label(frame)
            self.facedown.configure(image=img)
            self.facedown.image = img
            self.facedown.place(x=self.cardX, y=self.getCardY())

    def clearHand(self):
        for card in self.hand:
            card.getLabel().destroy()
        self.hand = []
        self.cardX = self.seats[self.seat][0]
        self.cardY = self.seats[self.seat][1]

    def getHandValue(self):
        value = 0
        count = 0
        for card in self.hand:
            value += card.getValue()
            if card.face=='A':
                count += 1
        while value>21 and count>0:
            value -= 10
            count -= 1
        return value
    
    def setHitBtn(self, hitbtn):
        self.hitBtn = hitbtn
    
    def setPassBtn(self, passbtn):
        self.passBtn = passbtn

    def disableBtn(self):
        self.hitBtn['state']='disabled'
        self.passBtn['state']='disabled'

    def enableBtn(self):
        self.hitBtn['state']='normal'
        self.passBtn['state']='normal'
        
class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"
        self.winCount = 0
        self.seat = 'N'
        seats = {'W':(70, 300),'N':(300, 30),'S':(300, 500), 'E':(800, 300)}
        self.cardX = seats[self.seat][0]
        self.cardY = seats[self.seat][1]
        self.deck = Deck()
        self.hand = []

    def deal(self):
        return self.deck.nextCard()

    def shuffle(self):
        self.deck.shuffle()

    def hit(self, frame):
        self.facedown.destroy()
        value = self.getHandValue()
        while value < 17:
            self.addCardToHand(self.deal(), frame)
            value = self.getHandValue()

class Blackjack(TkinterBase):
    def buildWidget(self):
        self.init()
        self.dealBtn = tk.Button(self.root, text="Deal Card", command=self.deal)
        self.dealBtn.place(x=10, y=50)
        self.addBtn = tk.Button(self.root, text="Add Player", command=self.popupwin)
        self.addBtn.place(x=10, y=20)
        self.collectBtn = tk.Button(self.root, text="Collect", command=self.winner)
        self.collectBtn.place(x=10, y=80)
        tk.Label(self.root, text="Game result").place(x=900, y=10)
        tk.Label(self.root, text="Dealer win count: ").place(x=900, y=40)
        self.defaultPlayerList()
        self.initPlayers()
        
    def winner(self):
        dealerTotal = self.dealer.getHandValue()
        for player in self.playerList:
            playerTotal = player.getHandValue()
            if playerTotal>21:
                self.dealer.win()
            elif dealerTotal>21:
                player.win()
            elif playerTotal==dealerTotal:
                pass
            elif playerTotal>dealerTotal:
                player.win()
            else:
                self.dealer.win()
            player.clearHand()
        self.displayResult()
        self.dealBtn['state']="normal"
        self.collectBtn['state']='disabled'

    def displayResult(self):
        tk.Label(self.root, text=str(self.dealer.winCount)).place(x=1020, y=40)
        for index in range(3):
            player = self.playerList[index]
            tk.Label(self.root, text=str(player.winCount)).place(x=1020, y=70+index*30)

    def init(self):
        self.root.title("Blackjack Card Game")
        self.root.geometry('1240x768')
        self.playerList = []
        self.playerIndex = 0
        self.dealer = Dealer()
        self.dealer.shuffle()
    
    def defaultPlayerList(self):
        self.playerList.append(Player("John", "W"))
        self.playerList.append(Player("Rodney","S"))
        self.playerList.append(Player("Charles", "E"))
        self.playerList.append(self.dealer)
        self.addBtn['state']='disabled'
        self.collectBtn['state']='disabled'
        tk.Label(self.root, text='John win count: ').place(x=900, y=70)
        tk.Label(self.root, text='Rodney win count: ').place(x=900, y=100)
        tk.Label(self.root, text='Charles win count: ').place(x=900, y=130)
        

    def deal(self):
        player = self.playerList[self.playerIndex]
        card = self.dealer.deal()
        player.addCardToHand(card, self.root)
        if self.playerIndex==3 and len(player.hand)==2:
            self.playerList[0].enableBtn()
            self.dealBtn['state']='disabled'
        self.playerIndex += 1
        if self.playerIndex >= len(self.playerList):
            self.playerIndex = 0

    def addPlayer(self):
        name = self.entry.get()
        seat = self.listbox.curselection()
        item = self.listbox.get(seat[0])
        self.playerList.append(Player(name, item[0]))
        self.listbox.delete(seat[0])
        self.entry.delete(0,tk.END)

    def initPlayers(self):
        for player in self.playerList:
            tk.Label(self.root, text=player.name).place(x=player.cardX-30, y=player.cardY)
        player = self.playerList[0]
        hitBtn=tk.Button(self.root, text='Hit', command=lambda: self.hit(0))
        hitBtn.place(x=player.cardX-30, y=player.cardY+30)
        passBtn=tk.Button(self.root, text='Pass', command=lambda: self.pass_(0))
        passBtn.place(x=player.cardX-30, y=player.cardY+60)
        player.setHitBtn(hitBtn)
        player.setPassBtn(passBtn)
        player.disableBtn()

        player = self.playerList[1]
        hitBtn = tk.Button(self.root, text='Hit', command=lambda: self.hit(1))
        hitBtn.place(x=player.cardX-30, y=player.cardY+30)
        passBtn = tk.Button(self.root, text='Pass', command=lambda: self.pass_(1))
        passBtn.place(x=player.cardX-30, y=player.cardY+60)
        player.setHitBtn(hitBtn)
        player.setPassBtn(passBtn)
        player.disableBtn()
        
        player = self.playerList[2]
        hitBtn=tk.Button(self.root, text='Hit', command=lambda: self.hit(2))
        hitBtn.place(x=player.cardX-30, y=player.cardY+30)
        passBtn=tk.Button(self.root, text='Pass', command=lambda: self.pass_(2))
        passBtn.place(x=player.cardX-30, y=player.cardY+60)
        player.setHitBtn(hitBtn)
        player.setPassBtn(passBtn)
        player.disableBtn()

    def hit(self, index):
        player = self.playerList[index]
        card = self.dealer.deal()
        player.addCardToHand(card, self.root)

    def pass_(self, index):
        player = self.playerList[index]
        player.disableBtn()
        if index==2:
            self.dealer.hit(self.root)
            self.collectBtn['state']='normal'
            return
        player = self.playerList[index+1]
        player.enableBtn()
        self.playerIndex = 0

    def close(self):
        self.playerList.append(Dealer())
        self.top.destroy()

    def disable_event(self):
        pass

    def popupwin(self):
        self.top= tk.Toplevel(self.root)
        self.top.title("Add Player")
        self.top.geometry("250x100")
        self.top.protocol("WM_DELETE_WINDOW", self.disable_event)
        tk.Label(self.top, text="Enter player name").place(x=10, y=10)
        tk.Label(self.top, text="Player seat").place(x=10, y=30)
        self.entry = tk.Entry(self.top, width= 15)
        self.entry.place(x=120, y=10)
        self.listbox = tk.Listbox(self.top, width=15, height=4, selectmode=tk.SINGLE)
        self.listbox.insert(0, "West")
        self.listbox.insert(1, "South")
        self.listbox.insert(2, "East")
        self.listbox.place(x=120, y=30)
        tk.Button(self.top, text="add", command=self.addPlayer).place(x=80, y=60)
        tk.Button(self.top, text="close", command=self.close).place(x=10, y=60)

if __name__ == '__main__':
    Blackjack()
