from tkinter import *

class BaseWindow:
    def __init__(self, width=1024, height=768):
        self.root = Tk()
        self.root.title("Blackjack Game")
        self.root.geometry('x'.join([str(width), str(height)])) # Super VGA monitor
        self.root.iconbitmap("src/images/blackjack.ico")
        self.buildWidgets()
        self.root.mainloop()
    
    def buildWidgets(self):
        pass

if __name__ == '__main__':
    BaseWindow()