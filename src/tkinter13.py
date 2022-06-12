"""

"""
from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title("PythonGuides")
ws.geometry('350x200')

def display():
    choice  = var.get()
    if choice == 1:
       output = "Cold Beverage"

    elif choice == 2:
       output =  "Warm Beverage"
    
    else:
       output =  "Hot Beverage"
    
    return messagebox.showinfo('Beverage selected', f'You Selected {output}.')

var = IntVar()    

cold_bev = Radiobutton(ws, text="Cold Beverage", variable=var, value=1,command=display).grid(row=0, column=1)
warm_bev = Radiobutton(ws, text="Warm Beverage", variable=var, value=21,command=display).grid(row=0, column=2)
hot_bev = Radiobutton(ws, text="Hot Beverage", variable=var, value=31,command=display).grid(row=0, column=3)


ws.mainloop()