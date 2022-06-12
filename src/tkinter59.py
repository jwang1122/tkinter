import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Slider")
root.geometry('400x400')

v_var = tk.StringVar()
h_var = tk.StringVar()

def slide():
    v_var.set(f"vertical value: {vertical.get()}")
    h_var.set(f"horizontal value:{horizontal.get()}")

vertical = tk.Scale(root, from_=0, to=200)
vertical.pack()
horizontal = tk.Scale(root, from_=0, to=400, orient=tk.HORIZONTAL)
horizontal.pack()

tk.Label(root, textvariable=v_var).pack()
tk.Label(root, textvariable=h_var).pack()


tk.Button(root, text='get values', command=slide).pack()

root.mainloop()
