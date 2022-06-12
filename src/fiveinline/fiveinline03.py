from tkinterbase import *
from math import sqrt

class Board(Canvas):
    def __init__(self, parent, width=600, height=480):
        self.unit = 30
        Canvas.__init__(self, parent, width=width, height=height)
        self.points = [[(i*self.unit,j*self.unit) for i in range(1,16)] for j in range(1,16)]
        for i in range(15): # draw horizontal lines
            self.create_line(self.points[i][0][0], self.points[i][0][1], self.points[i][14][0], self.points[i][14][1])
        for i in range(15): # draw vertical lines
            self.create_line(self.points[0][i][0], self.points[0][i][1], self.points[14][i][0], self.points[14][i][1])
        self.configure(bg='#ccb862')
        self.white = True

    def click(self, event):
        self.white = not self.white
        # print(f"({event.x}, {event.y})")
        # print(self.getPoint(event.x, event.y))
        x, y = self.getPoint(event.x, event.y)
        if x and self.white:
            self.create_oval(x-10,y-10,x+10,y+10,fill='#FFFFFF')
        if x and not self.white:
            self.create_oval(x-10,y-10,x+10,y+10,fill='#000000')

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
        self.board.bind('<Button-1>', self.board.click)
        self.board.pack()


if __name__ == '__main__':
    FiveInLine()
