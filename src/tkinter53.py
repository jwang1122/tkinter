"""
button icon and image
pip install Pillow
homework: load images from a folder, display them by click button
@see imageViewer.py
"""

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Button and icon")
root.iconbitmap('src/tkinter/love-letter.ico')

img = ImageTk.PhotoImage(Image.open("src/tkinter/groom.png"))
quitBtn = tk.Button(root, text="Exit", command=root.quit)
quitBtn.pack()

lbl = tk.Label(root, image=img)
lbl.pack()

root.mainloop()