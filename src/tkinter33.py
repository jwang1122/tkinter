"""
mouse double click
"""
from tkinter import *

def hello(event):
    print("Single Click, Button-l") 
def quit(event):                           
    print("Double Click, so let's stop") 
    import sys; sys.exit() 

root = Tk()
root.geometry('200x150')
widget = Button(root, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit) 

widget.mainloop()