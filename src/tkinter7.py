"""
using Combox
"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x300')

my_str_var = tk.StringVar()

my_combobox = ttk.Combobox(
    root, textvariable = my_str_var,
    values=["JavaScript", "Java", "Python", "C++", "C#"])

text = tk.StringVar()
text.set("Hello, Select your programming language")
my_label = tk.Label(root, textvariable=text, font=("Arial Bold", 20))

def f(event):
    print("Selected language:", my_combobox.get())

def change(event):
    text.set(my_combobox.get())

my_combobox.bind("<<ComboboxSelected>>",func=change)

# my_combobox.pack()
# my_label.pack()
my_combobox.grid(row=0, column=0)
my_label.grid(row=1, column=0)

root.mainloop()
