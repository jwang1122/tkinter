'''
titled frame
'''
from tkinter import *
screen = Tk()
screen.title("Titled Frame")
screen.geometry('300x300')
 
labelframe_tk = LabelFrame(screen, text="Label Frame Title")
labelframe_tk.pack(fill="both", expand="yes", padx=10, pady=10)
 
inside = Label(labelframe_tk, text="Add whatever you like")
inside.pack()
 
screen.mainloop()