from tkinter import *

root = Tk()
root.title("My First Frame")
root.geometry("1024x768")
root.iconbitmap("images/blackjack.ico")
root.configure(bg='#568568')

def start():
    print("the function will be available soon...")

welcomeLbl = Label(root, text='Welcome to Our Blackjack Game!', bg='#568568', fg='#630A4A', font=('Arial Bold', 30)) #RGB in Hex
welcomeLbl.pack(pady=30)
mainImage = PhotoImage(file='images/animation.gif')
imageLbl = Label(root, image=mainImage)
imageLbl.pack()
startBtn = Button(root, text="Start", command=start)
startBtn.pack(pady=30)


root.mainloop()