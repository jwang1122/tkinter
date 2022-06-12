from tkinter import *

root = Tk()
root.title("My First Frame")
root.geometry("1024x768")
root.iconbitmap("images/blackjack.ico")
root.configure(bg='#568568')

playerName = StringVar()
playerName.set("John")

ctrl = Frame(root, bg='#568568')
Button(ctrl, text="Button 1").pack(side=LEFT)
Button(ctrl, text="Button 2").pack(side=LEFT)
Button(ctrl, text="Button 3").pack(side=LEFT)
Label(ctrl, text=" ", bg='#568568').pack(side=LEFT, padx=300)
Label(ctrl, text="Player: ", bg='#568568').pack(side=LEFT, padx=5)
Label(ctrl, textvariable=playerName, bg='#568568').pack(side=LEFT, padx=5)
Button(ctrl, text="Hit").pack(side=LEFT, padx=5)
Button(ctrl, text="Pass").pack(side=LEFT, padx=5)
ctrl.pack()
img = PhotoImage(file = "images/jokerR.gif")
Label(root, image = img).pack()
root.mainloop()