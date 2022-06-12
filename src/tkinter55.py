import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Radio button")

Topping = [
    ("Pepperoni",1),
    ("Cheese",2),
    ("Mushroom",3),
    ("Onion",4),
    ("Peper",5),
]

top = tk.StringVar()
top.set(3)

for text, topping in Topping:
    tk.Radiobutton(root, text=text, variable=top, value=topping).pack(anchor=tk.W) # anchor='w'

tk.Label(root, textvariable=top).pack(pady=10)

root.mainloop()