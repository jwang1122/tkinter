from tkinterbase import *

class Five:
    def __init__(self, isWin, start, end):
        self.isWin = isWin
        self.start = start
        self.end = end

    def draw(self):
        pass

class Chess:
    def __init__(self, x, y, board, size=30, color=None):
        self.xIndex, self.yIndex = x, y
        self.x, self.y = x*size, y*size
        self.size = size
        self.color = color
        self.board = board
    
    def __repr__(self):
        return f"({self.xIndex}, {self.yIndex})|{self.color}"
    
    def draw(self):
        self.board.create_oval(self.x-10,self.y-10,self.x+10,self.y+10,fill=self.color)

class Board(Canvas):
    def __init__(self, parent, width= 600, height=600, bg='#CDBA96', size=19):
        Canvas.__init__(self, parent, width=width, height=height)
        self.configure(bg=bg)
        self.chesses = [[Chess(i,j,self) for i in range(1,size+1)] for j in range(1,size+1)]
        self.drawChessBoard(size)
        self.size = size
        self.isBlack = True

    def drawChessBoard(self,size):
        for i in range(size): # draw horizontal lines
            self.create_line(self.chesses[i][0].x, self.chesses[i][0].y, self.chesses[i][size-1].x, self.chesses[i][size-1].y)
        for i in range(size): # draw vertical lines
            self.create_line(self.chesses[0][i].x, self.chesses[0][i].y, self.chesses[size-1][i].x, self.chesses[size-1][i].y)

    def clicked(self, event):
        chess = self.getChess(event.x, event.y)
        if chess:
            if self.isBlack: chess.color='black' 
            else: chess.color='white'
        chess.draw()
        self.takeTurn()
        v = self.fiveInLine()

    def fiveInLine(self):
        return Five(True, None, None)

    def getChess(self, mouseX, mouseY): # get the chess on mouse click position
        for i in range(self.size):
            for j in range(self.size):
                chess = self.chesses[i][j]
                distance = pow(pow((chess.x-mouseX),2) + pow((chess.y-mouseY),2), 0.5)
                if distance < 14:
                    return chess
        return None

    def takeTurn(self):
        self.isBlack = not self.isBlack
        
class FiveInLine(BaseWindow):
    def buildWidgets(self):
        self.board = Board(self.root)
        self.board.bind('<Button-1>', self.board.clicked)
        self.board.pack()

if __name__ == '__main__':
    FiveInLine()