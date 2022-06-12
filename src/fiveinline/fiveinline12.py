from tkinterbase import *

class Chess:
    def __init__(self, x, y, size=30, color=None):
        self.xIndex, self.yIndex = x, y
        self.x, self.y = x*size, y*size
        self.size = size
        self.color = color

class Board(Canvas):
    def __init__(self, parent, width= 600, height=600, bg='#CDBA96', size=19):
        Canvas.__init__(self, parent, width=width, height=height)
        self.configure(bg=bg)
        self.chesses = [[Chess(i,j) for i in range(1,size+1)] for j in range(1,size+1)]
        self.drawChessBoard(size)

    def drawChessBoard(self,size):
        for i in range(size): # draw horizontal lines
            self.create_line(self.chesses[i][0].x, self.chesses[i][0].y, self.chesses[i][size-1].x, self.chesses[i][size-1].y)
        for i in range(size): # draw vertical lines
            self.create_line(self.chesses[0][i].x, self.chesses[0][i].y, self.chesses[size-1][i].x, self.chesses[size-1][i].y)

    def clicked(self, event):
        print(f"({event.x}, {event.y})")

class FiveInLine(BaseWindow):
    def buildWidgets(self):
        self.board = Board(self.root)
        self.board.bind('<Button-1>', self.board.clicked)
        self.board.pack()

if __name__ == '__main__':
    FiveInLine()