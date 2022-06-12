from tkinter import*

def popupwin():
    global top
    global entry
    top = Toplevel(screen)
    top.geometry('300x250')
    top.title("set player's seat")
    entry = Entry(top, width=25)
    entry.pack()
    Button(top, text="get text", command=closewin).pack()

def closewin():
    global entry
    textVar.set(entry.get())
    top.destroy()

if __name__ == '__main__':
    screen = Tk()
    screen.geometry("600x480")
    screen.title("Popup window demo")
    textVar = StringVar()
    textVar.set("Show a popup window by click the button below.")
    lbl=Label(screen, textvariable=textVar)
    lbl.pack()
    Button(screen, text="Click Me", command=popupwin).pack()

    screen.mainloop()