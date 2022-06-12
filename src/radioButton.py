from tkinter import *

bg1 = '#FF0000'
rbl = []
def getSelected():
    bg1 = colorVar.get()
    root.configure(bg=bg1)
    lbl.configure(bg=bg1)
    for b in rbl:
        b.configure(bg=bg1)
    frame.configure(bg=bg1)

root = Tk()
root.geometry("600x400")
root.title("Radio Button")
colorVar = StringVar()
colorVar.set('#FF0000')
root.configure(bg=colorVar.get())
bgColors = [
    ("blue", '#0000FF'),
    ("red", '#FF0000'),
    ("yellow", '#FFFF00'),
    ("cyan", '#00FFFF'),
    ("gray", "#888888")
]
frame = Frame(root, bg=colorVar.get())
frame.pack()
for text, color in bgColors:
    b = Radiobutton(frame, text=text, variable=colorVar, value=color, command=getSelected,bg=colorVar.get())
    b.pack(anchor=W)
    rbl.append(b)

lbl = Label(root, textvariable=colorVar, fg='#FFFFFF', bg=colorVar.get())
lbl.pack()

root.mainloop()