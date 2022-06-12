from tkinter import *
from tkinter import font

class MainFrame():
    root = Tk()
    def __init__(self):
        self.root.title("Blackjack Game")
        self.root.geometry("1024x768")
        self.buildWidget()
        self.root.mainloop()

    def buildWidget(self):
        self.configFrame = ConfigFrame(self)
        self.boardFrame = BoardFrame(self)
        self.configFrame.pack(fill='both', expand=1)

    def switchToConfigFrame(self):
        self.configFrame.pack(fill='both', expand=1)
        self.boardFrame.pack_forget()

    def switchToBoardFrame(self):
        self.boardFrame.pack(fill='both', expand=1)
        self.configFrame.pack_forget()

class ConfigFrame(Frame):
    def __init__(self, parent):
        self.parent = parent
        Frame.__init__(self, parent.root)
        Label(self, text="Configur Frame").pack()
        Button(self, text="to Board Frame", command=self.switch).pack()
    
    def switch(self):
        self.parent.switchToBoardFrame()

class BoardFrame():
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent.root)
        Label(self.frame, text="Play Board Frame").pack()
        Button(self.frame, text="to Config Frame", command=self.switch).pack()

    def pack(self, **kwargs):
        self.frame.pack(kwargs)
  
    def pack_forget(self):
        self.frame.pack_forget()
        
    def switch(self):
        self.parent.switchToConfigFrame()

if __name__ == '__main__':
    MainFrame()
