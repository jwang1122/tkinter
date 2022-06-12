"""
Grid system
"""

import tkinter as tk

parent = tk.Tk()
parent.title("Grid system")
parent.geometry("640x480")

tk.Label(parent, text="Grid(0, 0)", bg='black', fg='white', padx=200).grid(row=0, column=0)
tk.Label(parent, text="Grid(0, 1)", bg='yellow', fg='black',pady=50).grid(row=0, column=1)
tk.Label(parent, text="Grid(0, 2)", bg='lightblue', fg='black',padx=200).grid(row=0, column=2)
tk.Label(parent, text="Grid(0, 1)", bg='pink', fg='black',padx=200).grid(row=1, column=1, columnspan=2)
tk.Label(parent, text="Grid(0, 3)", bg='pink', fg='black',pady=200).grid(row=0, column=3, rowspan=2)
# tk.Label(parent, text="pack()", bg='pink', fg='black',pady=200).pack() # once use grid() cannot use pack()
tk.Label(parent, text="place(100,100)", bg='pink', fg='black').place(x=100, y=100)


parent.mainloop()