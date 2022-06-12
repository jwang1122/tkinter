"""
using filedialog
"""
from tkinter import filedialog as fd
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('600x400')
text = tk.Text(root)

def openFile():
    filename = fd.askopenfilename()
    messagebox.showinfo("Selected File", filename)
    with open(filename) as f:
        t = f.read()
    text.insert("1.0", t)
    
openBtn = tk.Button(root, text='Open a File', command=openFile)
openBtn.pack(side="top")
text.pack()

tk.mainloop()
