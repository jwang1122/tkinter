import os
import tkinter as tk
from PIL import Image, ImageTk

path = r"C:/Users/12818/workspace/python-I/doc/images/"
dir_list = os.listdir(path)
count = len(dir_list)
imgList = []
dirList = list(filter(lambda filename: not filename.endswith('.svg'), dir_list))
print(dirList)

root = tk.Tk()
imgList = list(map(lambda filename: ImageTk.PhotoImage(Image.open(path + filename)), dirList))

currentIndex = 0
def previous():
    global currentIndex
    global lbl
    global dir_list
    global count
    currentIndex -= 1
    if currentIndex < 0:
        currentIndex = count-1
    img = imgList[currentIndex]
    lbl.config(image = img)
    lbl.image = img

def next():
    global currentIndex
    global lbl
    global dir_list
    global count
    currentIndex += 1
    if currentIndex == count:
        currentIndex = 0
    img = imgList[currentIndex]
    lbl.config(image = img)
    lbl.image = img


root.title("image viewer")
root.iconbitmap('src/tkinter/love-letter.ico')


img = ImageTk.PhotoImage(Image.open(path + dir_list[0]))
tk.Button(root, text="<<", command=previous).pack(side='left')
tk.Button(root, text="Exit", command=root.quit).pack()
tk.Button(root, text=">>", command=next).pack(side='right')

lbl = tk.Label(root, image=img)
lbl.pack()

root.mainloop()