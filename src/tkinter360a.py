from tkinter import *
from PIL import Image, ImageTk

root = Tk()
canvas = Canvas(root, width=640, height=480)
canvas.grid(columnspan=3)

logo = Image.open("src/tkinter/groom.png")
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)
root.mainloop()