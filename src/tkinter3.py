"""
change font of the label
"""
import tkinter as tk
parent = tk.Tk()
parent.title("-Welcome to Python tkinter")
parent.geometry('600x200')
parent.resizable(0,0)
myLabel1 = tk.Label(parent, text="Hello World!", font=("Arial Bold", 50))
myLabel1.pack()
myLabel2 = tk.Label(parent, text="My name is John Wang.",font=("Bradley Hand ITC", 30))
myLabel2.pack()
parent.mainloop()
