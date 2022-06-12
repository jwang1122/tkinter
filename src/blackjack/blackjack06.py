from tkinterbase import *

class Player:
    def __init__(self, name, seat):
        self.name = name
        self.seat = seat
    def __repr__(self) -> str:
        return self.name

class PlayBoard(TkinterBase):
    def buildWidget(self):
        self.root.title("Blackjack Game")
        self.bg = '#568568'
        self.buildControlFrame()
        self.buildBoardFrame()

    def buildControlFrame(self):
        self.root.configure(bg=self.bg)
        self.playerName = StringVar()
        self.playerName.set("Dealer")
        ctrl = Frame(self.root, bg=self.bg)
        Button(ctrl, text="Deal Card").pack(side=LEFT)
        Button(ctrl, text="Result").pack(side=LEFT)
        Button(ctrl, text="Configure").pack(side=LEFT)
        Label(ctrl, text=" ", bg=self.bg).pack(side=LEFT, padx=300)
        Label(ctrl, text="Player: ", bg=self.bg).pack(side=LEFT, padx=5)
        Label(ctrl, textvariable=self.playerName, bg=self.bg).pack(side=LEFT, padx=5)
        Button(ctrl, text="Hit").pack(side=LEFT, padx=5)
        Button(ctrl, text="Pass").pack(side=LEFT, padx=5)
        ctrl.pack()

    def buildBoardFrame(self):
        self.buildPlayerList()
        self.board = Frame(self.root, bg=self.bg)
        self.displayPlayerNames()
        self.board.pack()

    def displayPlayerNames(self):
        for player in self.playerList:
            Label(self.board, text=player.name, bg=self.bg).pack()

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