import tkinter as tk

class MyFrame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Blackjack")
        self.root.geometry("1024x768")
        self.createWidget()

        self.root.mainloop()

    def createWidget(self):
        tk.Button(self.root, text="Deal").place(x=100,y=100)
        
if __name__ == '__main__':
    MyFrame()
