from tkinter import*
from tkinter.ttk import Combobox
from turtle import width

screen = Tk()
screen.geometry("250x150")
screen.title("Player's name")
screen.configure(bg='yellow')
Label(screen, text="Player name:",bg='yellow').grid(row=0,column=0, pady=10)
Entry(screen, width=23).grid(row=0, column=1)
myText = StringVar()
myText.set("EAST")
Label(screen, text="Available Seats:",bg='yellow').grid(row=1, column=0)
combobox = Combobox(screen,textvariable=myText,values=["EAST","SOUTH","WEST"])
combobox.grid(row=1, column=1)
# textLbl = StringVar()
# Label(screen, textvariable=textLbl).pack()
setBtn = Button(screen, text="Set", width=20)
# setBtn.grid(row=4, column=0, columnspan=2, ipadx=35)
setBtn.place(x=60, y=120)

def change(event):
    text = myText.get()
    # textLbl.set(text)

combobox.bind("<<ComboboxSelected>>", func=change)
screen.mainloop()