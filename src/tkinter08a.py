from tkinter import *

root = Tk()
root.geometry('200x200+400+300')

boolean_python = BooleanVar()
boolean_java = BooleanVar()
boolean_C = BooleanVar()
selections = StringVar()

def cmd():
    selections.set("Your selections: \n")
    if boolean_python.get():
        selections.set(selections.get())
    if boolean_java.get():
        selections.set(selections.get() + "Java ")
    if boolean_C.get():
        selections.set(selections.get() + "C++ ")

Checkbutton(root, text="Good at Python", variable=boolean_python, command=cmd).pack(anchor='w')
Checkbutton(root, text="Good at Java", variable=boolean_java, command=cmd).pack(anchor='w')
Checkbutton(root, text="Good at C++", variable=boolean_C, command=cmd).pack(anchor='w')
Label(root, textvariable=selections).pack(anchor='w')

root.mainloop()
