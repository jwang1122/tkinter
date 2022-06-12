import tkinter as tk
from tkinter44 import *

class BlackjackGame(MyFrame):
    def createWidget(self):
       heartQ = tk.PhotoImage(file="images/heartQ.gif")
       lbl = tk.Label(self.root, image=heartQ)
       lbl.configure(image=heartQ)
       lbl.image = heartQ
       lbl.place(x = 10, y = 10)

if __name__ == '__main__':
    BlackjackGame()