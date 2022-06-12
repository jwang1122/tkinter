"""
using radio button and message box
"""
from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Applications')
ws.geometry('200x200+700+400')

def viewSelected():
    choice  = var.get()
    if choice == 1:
       output = "Science"

    elif choice == 2:
       output =  "Commerce"
    
    elif choice == 3:
       output =  "Arts"
    else:
        output = "Invalid selection"

    return messagebox.showerror('Application selected', f'You Selected {output}.')
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno    
var = IntVar()
Radiobutton(ws, text="Science", variable=var, value=1, command=viewSelected).pack(anchor='w')
Radiobutton(ws, text="Commerce", variable=var, value=2, command=viewSelected).pack(anchor='w')
Radiobutton(ws, text="Arts", variable=var, value=3, command=viewSelected).pack(anchor='w')

ws.mainloop()