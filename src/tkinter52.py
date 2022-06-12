"""
Place system
"""
from tkinter import *

parent = Tk()
parent.title("Place System")
parent.geometry('600x300')
parent.iconbitmap('src/tkinter/Screwdriver_Wrench.ico')


def todo():
    myLbl.config(text="You clicked the button...")

buttonImg = PhotoImage(file='src/tkinter/Screwdriver_Wrench.png')
imageBtn = Button(parent, image=buttonImg, command=todo, borderwidth=5)
imageBtn.pack(pady=10)

myLbl = Label(parent, text="")
myLbl.pack(pady=20)

parent.mainloop()