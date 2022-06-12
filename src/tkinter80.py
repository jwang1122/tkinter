from tkinter import *

root = Tk()
root.title("My First Frame")
root.geometry("1024x768")
root.iconbitmap("images/blackjack.ico")
root.configure(bg='#568568')

buttonFrm = Frame(root, bg='#568568')
Button(buttonFrm, text="Configure Player").grid(row=1,column=1)
Button(buttonFrm, text="Configure Background").grid(row=1,column=2)
Button(buttonFrm, text="Start", bg='#6E034C', fg='white').grid(row=2,column=1,columnspan=2,ipadx=100)
buttonFrm.pack(side=BOTTOM, pady=10)

root.mainloop()