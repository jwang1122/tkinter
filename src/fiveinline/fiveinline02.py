from turtle import width
from tkinterbase import *

class Board(Canvas):
    def __init__(self, parent, width= 600, height=480, bg='#CDBA96'):
        Canvas.__init__(self, parent, width=width, height=height)
        self.unit = 30
        self.configure(bg=bg)
        self.points = [[(i*self.unit,j*self.unit) for i in range(1,16)] for j in range(1,16)]
        self.drawChessBoard()

    def drawChessBoard(self):    
        for i in range(15): # draw horizontal lines
            self.create_line(self.points[i][0][0], self.points[i][0][1], self.points[i][14][0], self.points[i][14][1])
        for i in range(15): # draw vertical lines
            self.create_line(self.points[0][i][0], self.points[0][i][1], self.points[14][i][0], self.points[14][i][1])

    def click(self, event):
        print(f"({event.x}, {event.y})")

class FiveInLine(BaseWindow):
    def buildWidgets(self):
        self.board = Board(self.root)
        self.board.bind('<Button-1>', self.board.click)
        self.board.pack()

if __name__ == '__main__':
    FiveInLine()