"""
works, but not so efficient
duplicated code all over the place
"""

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image viewer")

img1=ImageTk.PhotoImage(Image.open("src/tkinter/groom.png"))
img2=ImageTk.PhotoImage(Image.open("src/tkinter/love-letter.png"))
img3=ImageTk.PhotoImage(Image.open("src/tkinter/Screwdriver_Wrench.png"))

imgList = [img1, img2, img3]

lbl = tk.Label(image=img1)
lbl.grid(row=0, column=0,columnspan=3)
imgIndex = 0

def forward(imgIndex):
    global lbl
    global buttonForward
    global buttonBack
    
    lbl.grid_forget() # get rid of image
    lbl = tk.Label(image=imgList[imgIndex-1])
    buttonForward = tk.Button(root, text='>>', command=lambda:forward(imgIndex+1))
    buttonBack = tk.Button(root, text='<<', command=lambda:back(imgIndex-1))

    if imgIndex==3:
        buttonForward = tk.Button(root, text='>>', state=tk.DISABLED)

    lbl.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)

def back(imgIndex):
    global lbl
    global buttonForward
    global buttonBack

    lbl.grid_forget() # get rid of image
    lbl = tk.Label(image=imgList[imgIndex-1])
    buttonForward = tk.Button(root, text='>>', command=lambda:forward(imgIndex+1))
    buttonBack = tk.Button(root, text='<<', command=lambda:back(imgIndex-1))

    if imgIndex==0:
        buttonBack = tk.Button(root, text='<<', state=tk.DISABLED)

    lbl.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)

buttonBack = tk.Button(root, text="<<", command=lambda:back)
buttonBack.grid(row=1, column=0)
buttonExit = tk.Button(root, text="Exit", command=root.quit)
buttonExit.grid(row=1, column=1)
buttonForward = tk.Button(root, text=">>", command=lambda :forward(2))
buttonForward.grid(row=1, column=2)

root.mainloop()