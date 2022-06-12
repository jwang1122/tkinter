from tkinter import *
from math import sqrt
import time

class BaseWindow:
    def __init__(self, width=700, height=720):
        self.root = Tk()
        self.root.title("Blackjack Game")
        self.root.geometry('x'.join([str(width), str(height)])) # Super VGA monitor
        self.root.iconbitmap("src/images/blackjack.ico")
        self.buildWidgets()
        self.root.mainloop()
    
    def buildWidgets(self):
        pass

class Board(Canvas):
    def __init__(self, parent, width=600, height=480):
        self.unit = 30
        Canvas.__init__(self, parent, width=width, height=height)
        self.parent = parent
        self.coordinates = [['empty' for i in range(15)] for j in range(15)]
        self.points = [[(i*self.unit,j*self.unit) for i in range(1,16)] for j in range(1,16)]
        for i in range(15): # draw horizontal lines
            self.create_line(self.points[i][0][0], self.points[i][0][1], self.points[i][14][0], self.points[i][14][1], width=2)
            self.create_line(self.points[i][0][0]+1, self.points[i][0][1]+1, self.points[i][14][0]+1, self.points[i][14][1]+1, width=1, fill='white')
        for i in range(15): # draw vertical lines
            self.create_line(self.points[0][i][0], self.points[0][i][1], self.points[14][i][0], self.points[14][i][1], width=2)
            self.create_line(self.points[0][i][0]+1, self.points[0][i][1]+1, self.points[14][i][0]+1, self.points[14][i][1]+1, width=1, fill='white')
        self.configure(bg='#ccb862')
        self.white = True

    def clicked(self, event):
        self.white = not self.white
        # print(f"({event.x}, {event.y})")
        # print(self.getPoint(event.x, event.y))
        x, y = self.getPoint(event.x, event.y)
        i = int(x/self.unit-1)
        j = int(y/self.unit-1)
        if x:
            if self.white:
                self.coordinates[i][j] = 'W'
                self.create_oval(x-10,y-10,x+10,y+10,fill='#FFFFFF')
            else:
                self.coordinates[i][j] = 'B'
                self.create_oval(x-10,y-10,x+10,y+10,fill='#000000')
        win, color = self.fiveInLine()
        if win: self.gameOver(color)
        time.sleep(0.2)

    def fiveInLine(self):
        win, color = self.checkAllRows() 
        if win:
            print(f"{color} Win!")
            return win, color
        win, color = self.checkAllColumns()
        if win:
            print(f"{color} Win!")
            return win, color
        win, color = self.checkBackSlash()
        if win:
            print(f"{color} Win!")
            return win, color
        win, color = self.checkForwardSlash()
        if win:
            print(f"{color} Win!")
            return win, color
        return False, 'empty'
        
    def checkAllColumns(self):
        count = 1
        a = 1
        for j in range(15):
            for i in range(15-4):
                curr = self.coordinates[i][j]
                while curr != 'empty' and a<5: 
                    if curr==self.coordinates[i+a][j]:
                        count += 1
                    a +=1
                if count == 5:
                    return True, curr
                else:
                    a, count = 1,1
        return False, None

    def checkAllRows(self):
        count = 1
        a = 1
        for i in range(15):
            for j in range(15-4):
                curr = self.coordinates[i][j]
                while curr != 'empty' and a<5: 
                    if curr==self.coordinates[i][j+a]:
                        count += 1
                    a +=1
                if count == 5:
                    return True, curr
                else:
                    a, count = 1,1
        return False, None

    def checkBackSlash(self):
        count = 1
        a = 1
        for i in range(15-4):
            for j in range(15-4):
                curr = self.coordinates[i][j]
                while curr != 'empty' and a<5: 
                    if curr==self.coordinates[i+a][j+a]:
                        count += 1
                    a +=1
                if count == 5:
                    return True, curr
                else:
                    a, count = 1,1
        return False, None

    def checkForwardSlash(self):
        count = 1
        a = 1
        for i in range(14, 4, -1):
            for j in range(15-4):
                curr = self.coordinates[i][j]
                while curr != 'empty' and a<5: 
                    if curr==self.coordinates[i-a][j+a]:
                        count += 1
                    a +=1
                if count == 5:
                    return True, curr
                else:
                    a, count = 1,1
        return False, None

    def gameOver(self, color):
        image = PhotoImage(file='src/images/gameover1.png')
        imgLbl = Label(self.parent, text='Game Over')
        imgLbl.configure(image=image)
        imgLbl.image = image
        imgLbl.pack()
        lbl = Label(self)
        if color=="B":
            lbl.configure(text="Black Win!", fg='blue', bg='#ccb862', font=("Arial Bold", 16))
        else:
            lbl.configure(text="White Win!", fg='blue', bg='#ccb862', font=("Arial Bold", 16))
        lbl.place(x=460, y=200)

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
    FiveInLine()
