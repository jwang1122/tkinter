"""
using list box
"""
import tkinter as tk

parent = tk.Tk()
parent.geometry("250x300")
label1 = tk.Label(parent,text = "A list of favourite languages...")

listbox = tk.Listbox(parent, width=40, height=10, selectmode=tk.MULTIPLE)
listbox.insert(1, "PHP")
listbox.insert(2, "Python")
listbox.insert(3, "Java")
listbox.insert(4, "C#")
label1.pack()
listbox.pack()

def selectedItem():
    for i in listbox.curselection():
        print(str(listbox.get(i)))

btn = tk.Button(parent, text="Print Selected", command=selectedItem)

btn.pack(side='bottom')

parent.mainloop()
