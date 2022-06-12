from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
from math import sqrt
from playsound import playsound
from threading import *

def play():
    playsound('src/fiveinline/yunque.mp3')

def threading():
    t1 = Thread(target=play)
    t1.start()

class BaseWindow:
    def __init__(self, width=700, height=720):
        self.root = Tk()
        self.root.title("Blackjack Game")
        self.root.geometry('x'.join([str(width), str(height)])) # Super VGA monitor
        self.root.iconbitmap("src/images/blackjack.ico")
        self.buildWidgets()
        # self.root.mainloop()
    
    def buildWidgets(self):
        pass

class Board(Canvas):
    def __init__(self, parent, width=600, height=480):
        Canvas.__init__(self, parent, width=width, height=height)
        self.parent = parent
        self.blackwinImg = PhotoImage(file='src/images/blackwin.png')
        self.wCount, self.bCount = 0,0
        self.chessPieces = [[None for i in range(15)] for j in range(15)]
        self.unit = 30
        self.points = [[(i*self.unit,j*self.unit) for i in range(1,16)] for j in range(1,16)]
        for i in range(15): # draw horizontal lines
            self.create_line(self.points[i][0][0], self.points[i][0][1], self.points[i][14][0], self.points[i][14][1], width=2)
            self.create_line(self.points[i][0][0]+1, self.points[i][0][1]+1, self.points[i][14][0]+1, self.points[i][14][1]+1, width=1, fill='white')
        for i in range(15): # draw vertical lines
            self.create_line(self.points[0][i][0], self.points[0][i][1], self.points[14][i][0], self.points[14][i][1], width=2)
            self.create_line(self.points[0][i][0]+1, self.points[0][i][1]+1, self.points[14][i][0]+1, self.points[14][i][1]+1, width=1, fill='white')
        self.configure(bg='#ccb862')
        self.white =  True # Black go first
        self.isGameover = False
        # self.t = time.time()
        # self.t1 = time.time()-0.2

    def clicked(self, event):
        # self.t = time.time()
        # if self.t - self.t1 > 0.2:
        if self.isGameover: return
        self.white = not self.white
        x, y = self.getPoint(event.x, event.y)
        i = int(x/self.unit-1)
        j = int(y/self.unit-1)
        if x:
            if self.white:
                self.chessPieces[i][j], self.wCount = 'White', self.wCount + 1
                self.create_oval(x-10,y-10,x+10,y+10,fill='#FFFFFF')
            else:
                self.chessPieces[i][j], self.bCount = 'Black', self.bCount + 1
                self.create_oval(x-10,y-10,x+10,y+10,fill='#000000')
        blackLbl = Label(self)
        blackLbl.configure(text=f"Black: {self.bCount}", bg='#ccb862', font=("Arial Bold", 12))
        blackLbl.place(x=460, y=20)        
        whiteLbl = Label(self)
        whiteLbl.configure(text=f"White: {self.wCount}", bg='#ccb862', font=("Arial Bold", 12))
        whiteLbl.place(x=460, y=50)        
        win, color = self.fiveInLine()
        if win: self.gameOver(color)
        # self.t1 = self.t
        
    def fiveInLine(self):
        win, color = self.checkAllRows() 
        if win: return win, color
        win, color = self.checkAllColumns()
        if win: return win, color
        win, color = self.checkBackSlash()
        if win: return win, color
        win, color = self.checkForwardSlash()
        if win: return win, color
        return False, None
        
    def checkAllColumns(self):
        for j in range(15):
            for i in range(11):
                a, count = 1,1
                curr = self.chessPieces[i][j]
                while curr and a<5: 
                    if curr==self.chessPieces[i+a][j]:
                        count += 1
                    a +=1
                if count == 5:
                    return True, curr
        return False, None

    def checkAllRows(self):
        for i in range(15):
            for j in range(11):
                a, count = 1,1
                curr = self.chessPieces[i][j]
                while curr and a<5: 
                    if curr==self.chessPieces[i][j+a]:
                        count += 1
                    a +=1
                if count == 5:
                    return True, curr
        return False, None

    def checkBackSlash(self):
        for i in range(11):
            for j in range(11):
                a, count = 1,1
                curr = self.chessPieces[i][j]
                while curr and a<5: 
                    if curr==self.chessPieces[i+a][j+a]:
                        count += 1
                    a +=1
                if count == 5:
                    return True, curr
        return False, None

    def checkForwardSlash(self):
        for i in range(14, 3, -1):
            for j in range(11):
                a, count = 1,1
                curr = self.chessPieces[i][j]
                while curr and a<5: 
                    if curr==self.chessPieces[i-a][j+a]:
                        count += 1
                    a +=1
                if count == 5:
                    return True, curr
        return False, None

    def gameOver(self, color):
        self.isGameover = True
        self.create_image(300, 235, image=self.blackwinImg)
        image = PhotoImage(file='src/images/gameover1.png')
        imgLbl = Label(self.parent, text='Game Over')
        imgLbl.configure(image=image)
        imgLbl.image = image
        imgLbl.pack()

    def getPoint(self, x, y):
        for i in range(15):
            for j in range(15):
                x1 = self.points[i][j][0]
                y1 = self.points[i][j][1]
                r = sqrt(pow((x1-x),2) + pow((y1-y),2))
                if r<14:
                    return x1, y1
        return None, None

class FiveInLine(BaseWindow):    
    def buildWidgets(self):
        self.board = Board(self.root)
        self.board.bind('<ButtonRelease-1>', self.board.clicked)
        self.board.pack()

if __name__ == '__main__':
    threading()
    FiveInLine().root.mainloop()
