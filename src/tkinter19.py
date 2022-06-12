"""
using dialog
"""
from tkinter.simpledialog import *
import tkinter as tk

frame = tk.Tk()
frame.title("Main Window")

text = tk.StringVar()
text.set("your value here")
valueLabel = tk.Label(frame, textvariable=text)
valueLabel.place(x=10, y=10)

dialog1 = askfloat("Simple Dialog", "Enter a float")

text.set(dialog1)

mainloop()