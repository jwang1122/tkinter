import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Slider")
root.geometry('400x250')

v_var = tk.StringVar()
h_var = tk.StringVar()

def v_slide(var):
    v_var.set(f"vertical value: {var}")
def h_slide(var):
    h_var.set(f"horizontal value:{var}")

tk.Scale(root, from_=150, to=0, label="°F", command=v_slide).pack(anchor='e')
tk.Scale(root, from_=0, to=400, orient=tk.HORIZONTAL, label="Distance",length=390,command=h_slide).pack()
tk.Label(root, textvariable=v_var).pack()
tk.Label(root, textvariable=h_var).pack()

root.mainloop()
