from tkinter import *
from blackjackgif import ImageLabel

root = Tk()
root.title("My First Frame")
root.geometry("1024x768")
root.iconbitmap("images/blackjack.ico")
root.configure(bg='#568568')

def start():
    print("the function will be available soon...")

welcomeLbl = Label(root, text='Welcome to Our Blackjack Game!', bg='#568568', fg='#630A4A', font=('Arial Bold', 30)) #RGB in Hex
welcomeLbl.pack(pady=30)
# mainImage = PhotoImage(file='images/animation.gif', format='gif -index 1')
# imageLbl = Label(root, image=mainImage)
# imageLbl.pack()
lbl = ImageLabel(root)
lbl.pack()
lbl.load('images/animation.gif')
confFrame = Frame(root, bg='#568568')
btn1= Button(confFrame, text="Configure Players")
btn1.grid(row=1, column=1)
Button(confFrame, text="Configure Background").grid(row=1, column=2)
startBtn = Button(confFrame, text="Start", width=32, bg='#6E034C', fg='white', command=start)
startBtn.grid(row=2, column=1, columnspan=2, pady=10)
confFrame.pack(pady=30)

root.mainloop()