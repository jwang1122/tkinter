from tkinter import *

class BaseWindow():
    root = Tk()
    def __init__(self, title="Game", width=1024, height=768):
        self.root.title(title)
        self.root.geometry('x'.join([str(width), str(height)])) # Super VGA monitor
        self.root.iconbitmap("src/images/blackjack.ico")
        self.buildWidgets()
        self.root.mainloop()
    
    def buildWidgets(self):
        pass

if __name__ == '__main__':
    BaseWindow()