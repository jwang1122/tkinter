from tkinter import *

root = Tk()
root.geometry("500x300")
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(side=LEFT)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(side=LEFT)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(side=LEFT)

root.mainloop()