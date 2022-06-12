"""
using form
"""
import tkinter as tk

class MyFrame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sign up form")
        self.root.geometry("400x250")

        self.prompt = tk.Label(self.root, text="Please sign up:",  font=("Arial Bold", 14))
        self.prompt.place(x=25, y=10)
        self.name = tk.Label(self.root, text = "Name")
        self.name.place(x = 30, y = 50)
        self.email = tk.Label(self.root, text = "User ID")
        self.email.place(x = 30, y = 90)
        self.password =  tk.Label(self.root, text = "Password")
        self.password.place(x = 30, y = 130)
        self.sbmitbtn = tk.Button(self.root, text = "Submit", activebackground = "green", activeforeground = "blue", command=self.display)
        self.sbmitbtn.place(x = 120, y = 170)
        self.entry1 = tk.Entry(self.root)
        self.entry1.place(x = 85, y = 50)
        self.entry2 = tk.Entry(self.root)
        self.entry2.place(x = 85, y = 90)
        self.entry3 = tk.Entry(self.root)
        self.entry3.place(x = 90, y = 130)

        self.root.mainloop()

    def display(self):
        print(f"Name: {self.entry1.get()}; Email: {self.entry2.get()}; Password: {self.entry3.get()}.")

if __name__ == '__main__':
    MyFrame()