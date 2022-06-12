"""
Simple add calculator
"""

import tkinter as tk

value = 0
def number(n):
    e.insert(tk.END, n)    

def add():
    global value
    value += int(e.get())
    e.delete(0, tk.END)

def clear():
    global value
    e.delete(0, tk.END)
    value = 0

def equal():
    global value
    value += int(e.get())
    e.delete(0, tk.END)
    e.insert(0, value)

root = tk.Tk()
root.title("Simple Calculator")

e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0,columnspan=3, padx=10, pady=10)

btn1= tk.Button(root, text="1", padx=40, command=lambda: number(1))
btn2= tk.Button(root, text="2", padx=40, command=lambda: number(2))
btn3= tk.Button(root, text="3", padx=40, command=lambda: number(3))
btn4= tk.Button(root, text="4", padx=40, command=lambda: number(4))
btn5= tk.Button(root, text="5", padx=40, command=lambda: number(5))
btn6= tk.Button(root, text="6", padx=40, command=lambda: number(6))
btn7= tk.Button(root, text="7", padx=40, command=lambda: number(7))
btn8= tk.Button(root, text="8", padx=40, command=lambda: number(8))
btn9= tk.Button(root, text="9", padx=40, command=lambda: number(9))
btn0= tk.Button(root, text="0", padx=40, command=lambda: number(0))
btnAdd = tk.Button(root, text="+", padx=39, command=add)
btnEqual = tk.Button(root, text="=", padx=87, command=equal)
btnClear = tk.Button(root, text="Clear", padx=77, command=clear)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)
btnClear.grid(row=4, column=1, columnspan=2)
btnAdd.grid(row=5, column=0)
btnEqual.grid(row=5, column=1, columnspan=2)

root.mainloop()
