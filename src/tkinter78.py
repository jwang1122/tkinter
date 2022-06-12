from tkinter import *

root = Tk()

root.geometry("500x300")
frm = Frame(root)
w = Label(frm, text="Red Sun", bg="red", fg="white")
w.pack(side=LEFT)
w = Label(frm, text="Green Grass", bg="green", fg="black")
w.pack(side=LEFT)
w = Label(frm, text="Blue Sky", bg="blue", fg="white")
w.pack(side=LEFT)
frm.pack(side=TOP)

root.mainloop()