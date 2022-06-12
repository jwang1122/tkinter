import tkinter as tk
import random

root = tk.Tk()
root.geometry('1024x768')
x = 10
step = 30

def deal():
    global x
    card = deck.next()
    img = card.getImage()
    lbl = tk.Label(root, image=img)
    lbl.configure(image=img)
    lbl.image = img
    x += step
    lbl.place(x = x , y = 10)

dealBtn = tk.Button(root, text="Deal Card", command=deal).place(x=5, y=300) 

class Deck:
    suits = ['spade','club','diamond','heart']
    faces = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

    def __init__(self):
        self.stackOfCards = [Card(face, suit) for face in self.faces for suit in self.suits]
        random.shuffle(self.stackOfCards)
        self.currentIndex = 52

    def next(self):
        self.currentIndex -= 1
        return self.stackOfCards[self.currentIndex]

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return '('+self.face+', '+self.suit+')'

    def getImage(self):
        filename = 'images/' + self.suit + self.face+'.gif'
        image = tk.PhotoImage(file=filename)
        return image

deck = Deck()

card = deck.next()
img = card.getImage()
lbl1 = tk.Label(root, image=img)
lbl1.place(x = x, y = 10)


root.mainloop()
