from tkinter import*

screen = Tk()
screen.geometry("300x250")
Label(screen, text="A list of favourite languages...").pack()
listBox = Listbox(screen, width=40, height=10, selectmode=MULTIPLE)
listBox.insert(1, "PHP")
listBox.insert(2, "Python")
listBox.insert(3, "Java")
listBox.insert(4, "C++")
listBox.pack()

def selectedItem():
    for i in listBox.curselection():
        print(listBox.get(i))

Button(screen, text='Get selected language', command=selectedItem).pack()

screen.mainloop()