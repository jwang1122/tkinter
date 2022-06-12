from tkinter import *

root = Tk()
root.title("My First Frame")
root.geometry("1024x768")
root.iconbitmap("images/blackjack.ico")
root.configure(bg='#568568')

Button(root, text="Start").pack(side=BOTTOM)
buttonFrm = Frame(root)
Button(buttonFrm, text="Configure Player").pack(side=LEFT)
Button(buttonFrm, text="Configure Background").pack(side=LEFT)
buttonFrm.pack(side=BOTTOM)

root.mainloop()