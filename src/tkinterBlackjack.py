"""
Basic Blackjack Card Game GUI: Graphics User Interface
"""

import tkinter as tk
from PIL import ImageTk
import random

class Card:

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return f"({self.face}, {self.suit})"

    def getImage(self):
        filename = f'images/{self.suit}{self.face}.gif'
        return ImageTk.PhotoImage(file=filename)


class Player:
    seats = {'W':(70, 300), 'N':(300, 30), 'S':(300, 500), 'E':(800, 300)}
    def __init__(self, name, seat):
        self.name = name
        self.seat = seat[0]
        self.cardX = self.seats[self.seat][0]
        self.cardY = self.seats[self.seat][1]

    def __repr__(self):
        return f"{self.name}:{self.seat}"

    def getCardX(self):
        self.cardX += 30
        return self.cardX
    
    def getCardY(self):
        return self.cardY

class Dealer(Player):
    def __init__(self):
        self.name = 'Dealer'
        self.seat = 'N'
        self.cardX = Player.seats[self.seat][0]
        self.cardY = Player.seats[self.seat][1]

class Game():
    suits = ['spade','club','diamond','heart']
    faces = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Blackjack")
        self.root.geometry('1240x768')
        self.createWidgets()
        self.init()

        self.root.mainloop()

    def init(self):
        self.cards = [Card(face, suit) for face in self.faces for suit in self.suits]
        random.shuffle(self.cards)
        self.currentIndex = 52
        self.playerList = []
        self.playIndex = 0

    def createWidgets(self):
        tk.Button(self.root, text="Deal Card", command=self.deal).place(x=10, y=50)
        tk.Button(self.root, text="Add Player", command=self.popupwin).place(x=10, y=20)

    def popupwin(self):
        self.top = tk.Toplevel(self.root)
        self.top.title("Add Player")
        self.top.geometry("250x100")
        # self.root.protocol("WM_DELETE_WINDOW", self.diable_event)
        tk.Label(self.top, text="Enter player name").place(x=10, y=10)
        tk.Label(self.top, text="Player seat").place(x=10, y=30)
        self.name = tk.Entry(self.top, width=15)
        self.name.place(x=120, y=10)
        self.listbox = tk.Listbox(self.top, width=15, height=4, selectmode=tk.SINGLE)
        self.listbox.insert(0,"West") # (value, display)
        self.listbox.insert(1, "South")
        self.listbox.insert(2, "East")
        self.listbox.place(x=120, y=30)
        tk.Button(self.top, text="Add", command=self.addPlayer).place(x=80, y=60)
        tk.Button(self.top, text="End", command=self.close).place(x=10, y=60)

    def addPlayer(self):
        name = self.name.get()
        index = self.listbox.curselection() # seat include value, and display string
        seat = self.listbox.get(index[0])
        player = Player(name, seat)
        self.listbox.delete(index[0])
        self.name.delete(0, tk.END)
        self.playerList.append(player)
        
    def deal(self):
        player = self.playerList[self.playIndex]
        self.currentIndex -= 1
        card = self.cards[self.currentIndex]
        img = card.getImage()
        label = tk.Label(self.root)
        label.configure(image=img)
        label.image = img
        label.place(x=player.getCardX(), y=player.getCardY())
        self.playIndex +=1
        if self.playIndex >= len(self.playerList):
            self.playIndex = 0

    def close(self):
        self.playerList.append(Dealer())
        self.top.destroy()

if __name__ == '__main__':
    window = Game()