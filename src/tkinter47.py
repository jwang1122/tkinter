"""
use tkinter Entry
"""

import tkinter as tk

def click():
    text.insert(1.0,e.get()) # get content from entry

def clear():
    e.delete(0,tk.END)

root = tk.Tk()
root.geometry('300x120')
label = tk.Label(root,text="Enter player name")
label.place(x=10, y=10)
e = tk.Entry(root)
e.place(x=120, y=10)
okBtn = tk.Button(root, text='OK', command=click)
okBtn.place(x=120, y=30)
clearBtn = tk.Button(root, text='Clear', command=clear)
clearBtn.place(x=180, y=30)
text = tk.Text(root, height=3, width=35)
text.place(x=10, y=50)

root.mainloop()