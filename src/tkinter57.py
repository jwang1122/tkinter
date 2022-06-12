from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Message box')
ws.geometry('200x200+700+400')

response=StringVar()

def popup():
    response.set(messagebox.askokcancel("question","Do you want to continue?"))

Button(ws, text="popup", command=popup).pack()
Label(ws, textvariable=response).pack()

ws.mainloop()
