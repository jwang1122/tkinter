from tkinterbase import *

class Player:
    seats = {'WEST':(70, 300),'NORTH':(300, 30),'SOUTH':(300, 500), 'EAST':(650, 300)}
    def __init__(self, name, seat='EAST'):
        self.name = name
        self.seat = seat
        self.winCount = 0
        self.seat = seat
        self.hand = []
        self.cardX = self.seats[seat][0]
        self.cardY = self.seats[seat][1]

    def getX(self):
        return self.cardX

    def getY(self):
        return self.cardY

    def __repr__(self) -> str:
        return self.name

class PlayBoard(BaseWindow):
    def buildWidgets(self):
        self.root.title("Blackjack Game")
        self.bg = '#568568'
        self.buildControlFrame()
        self.buildBoardFrame()

    def buildControlFrame(self):
        self.root.configure(bg=self.bg)
        self.playerName = StringVar()
        self.playerName.set("Dealer")
        ctrl = Frame(self.root, bg=self.bg)
        Button(ctrl, text="Deal Card").pack(side=LEFT, padx=3)
        Button(ctrl, text="Result").pack(side=LEFT, padx=3)
        Button(ctrl, text="Configure").pack(side=LEFT, padx=3)
        Label(ctrl, text=" ", bg=self.bg).pack(side=LEFT, padx=300)
        Label(ctrl, text="Player: ", bg=self.bg).pack(side=LEFT, padx=5)
        Label(ctrl, textvariable=self.playerName, bg=self.bg).pack(side=LEFT, padx=5)
        Button(ctrl, text="Hit").pack(side=LEFT, padx=3)
        Button(ctrl, text="Pass").pack(side=LEFT, padx=3)
        ctrl.pack()

    def buildBoardFrame(self):
        self.buildPlayerList()
        self.displayPlayerNames()

    def displayPlayerNames(self):
        for player in self.playerList:
            Label(self.root, text=player.name, bg=self.bg).place(x=player.getX()-50, y=player.getY())

    def buildPlayerList(self):
        self.playerList = []
        player = Player("East", "EAST")
        self.playerList.append(player)
        player = Player("South", "SOUTH")
        self.playerList.append(player)
        player = Player("West", "WEST")
        self.playerList.append(player)
        player = Player("Dealer", "NORTH")
        self.playerList.append(player)
        

if __name__ == '__main__':
    PlayBoard()