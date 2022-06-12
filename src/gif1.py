from threading import Timer
from tkinter import *
from PIL import Image, ImageTk
from time import sleep

root = Tk()

file = 'images/animation.gif'
info = Image.open(file)
frameCount = info.n_frames
# print(frameCount)
frames = [PhotoImage(file=file, format=f'gif -index {i}') for i in range(frameCount)]
frame = 1

def show(label, photo):
    sleep(0.05)
    label.configure(image = photo)
    label.image = photo

def run_animation():
    while True:
        global frames
        global frame
        global label
        photo = frames[frame]
        show(label, photo)

        frame = frame + 1
        if frame == frameCount:
            frame = 1

label = Label(image = frames[0])
lbl = Label(image = frames[1])
animate = Button(
    root,
    text = "animate",
    command = run_animation
    )

label.place()
animate.pack()

root.mainloop()