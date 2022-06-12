"""
card game gui
"""
import tkinter as tk
from PIL import Image, ImageTk
import random

class Card:
    suits = ["spade","club","diamond","heart"]
    faces = ["A",'2','3','4','5','6','7','8','9','10','J',"Q",'K']

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
    
    def __repr__(self):
        return '('+self.face+', '+self.suit+')'
    
    def getImage(self):
        filename = "images/"+self.suit+self.face+".gif"
        image = ImageTk.PhotoImage(file=filename)
        return image
    

class Player:
    def __init__(self, name, seat='W'):
        self.name = name
        self.seat = seat
        seats = {'W':(70, 300),'N':(300, 30),'S':(300, 500), 'E':(800, 300)}
        self.cardX = seats[seat][0]
        self.cardY = seats[seat][1]

    def __repr__(self):
        return self.name

    def getCardX(self):
        self.cardX += 30
        return self.cardX
    
    def getCardY(self):
        return self.cardY

class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"
        self.seat = 'N'
        seats = {'W':(70, 300),'N':(300, 30),'S':(300, 500), 'E':(800, 300)}
        self.cardX = seats[self.seat][0]
        self.cardY = seats[self.seat][1]

class MyFrame():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Blackjack Card Game")
        self.root.geometry('1240x768')
        self.create_widgets()
        self.playerList = []
        self.cards = [Card(face, suit) for face in Card.faces for suit in Card.suits]
        random.shuffle(self.cards)
        self.currentIndex = 52
        self.playerIndex = 0

        self.root.mainloop()

    def create_widgets(self):
        self.dealBtn = tk.Button(self.root, text="Deal Card", command=self.deal)
        self.dealBtn.place(x=10, y=50)
        self.addBtn = tk.Button(self.root, text="Add Player", command=self.popupwin)
        self.addBtn.place(x=10, y=20)

    def deal(self):
        # for player in self.playerList:
        self.currentIndex -= 1
        player = self.playerList[self.playerIndex]
        card = self.cards[self.currentIndex]
        img = card.getImage()
        label = tk.Label(self.root)
        label.configure(image=img)
        label.image = img
        label.place(x=player.getCardX(), y=player.getCardY())
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
    game = MyFrame()
