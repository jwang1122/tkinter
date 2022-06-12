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
        Button(self.root, text="Deal Card").pack()
        self.buildPlayerList()
        self.displayPlayerNames()

    def displayPlayerNames(self):
        for player in self.playerList:
            Label(self.root, text=player.name).pack()

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