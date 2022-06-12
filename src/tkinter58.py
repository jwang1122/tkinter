from tkinter import *
from PIL import Image, ImageTk

ws = Tk()
ws.title('Main Frame')
ws.geometry('600x450+700+400')
ws.iconbitmap('src/tkinter/love-letter.ico')

img = Image.open("src/tkinter/groom.png")
print(img.size) # get original image size

img = img.resize((400, 400))
img = ImageTk.PhotoImage(img)
Label(ws, image=img).pack()

def open():
    top = Toplevel()
    Label(top, text='Hello').pack()

Button(ws, text='Open', command=open).pack()

ws.mainloop()