from tkinter import *
from PIL import ImageTk # Pillow module
import random
import sys
from tkinter.ttk import Combobox
from blackjackgif import ImageLabel

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

# common function to enable or disable buttons
def setButtonEnabled(btn, flag):
    if(flag):
        btn['state'] = 'normal'
    else:
        btn['state'] = 'disabled'

class Player:
    seatLocation = {"EAST":(600, 300), "SOUTH":(300, 550), "WEST":(70, 300), "NORTH":(300, 30)}
    def __init__(self, name, seat, screen):
        self.name = name
        self.seat = seat
        self.screen = screen
        self.hand = []
        self.winCount = 0
        self.cardX = Player.seatLocation[seat][0]
        self.cardY = Player.seatLocation[seat][1]
        self.nameVar = StringVar()
        self.nameVar.set(self.name)
        self.winVar = StringVar()
        self.winVar.set(self.winCount)

    def updateWinCount(self):
        self.winVar.set(self.winCount)
        
    def win(self):
        self.winCount += 1

    def __repr__(self) -> str:
        return self.name

    def addCardToHand(self, card): # display the card image
        self.hand.append(card)
        cardImage = card.getImage()
        lbl = Label(self.screen)
        lbl.configure(image=cardImage)
        lbl.image = cardImage
        lbl.place(x=self.getCardX(), y=self.getCardY())
        self.screen.cardLbls.append(lbl)
        if self.name=="Dealer" and len(self.hand)==2: # disable deal button
            imgFile = 'src/images/backR.gif'
            facedown = ImageTk.PhotoImage(file=imgFile)
            self.screen.facedownLbl = Label(self.screen)
            self.screen.facedownLbl.configure(image=facedown)
            self.screen.facedownLbl.image = facedown
            self.screen.facedownLbl.place(x=self.getCardX(), y=self.getCardY())
        self.cardX += 30

    def getCardX(self):
        return self.cardX

    def getCardY(self):
        return self.cardY

    def getHandValue(self): # handle all possible Ace
        value = 0
        count = 0 # count how many Ace in your hand
        for card in self.hand:
            value += card.getValue()
            if card.face=='A':
                count += 1
        while value>21 and count>0:
            value -= 10 # make A=1
            count -= 1
        return value

    def clearHand(self):
        self.hand.clear()
        # print(f"{self.name}: {self.hand}")

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        imgFile = 'src/images/' + self.suit + self.face + '.gif'
        self.image = ImageTk.PhotoImage(file=imgFile)

    def __repr__(self):
        return f"Card({self.face}, {self.suit})"

    def getValue(self):
        imgcard = {"A":11,"J":10,"Q":10,"K":10}
        if self.face in ["A","J","Q","K"]:
            return imgcard[self.face]
        return int(self.face)

    def getImage(self):
        return self.image

class Deck:
    faces = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
    suits = ('spade','club','diamond','heart')

    def __init__(self):
        self.currentIndex = 52
        self.cards = [Card(face,suit) for face in  self.faces for suit in self.suits]
        self.shuffle()

    def next(self):
        self.currentIndex -= 1
        return self.cards[self.currentIndex]

    def shuffle(self):
        random.shuffle(self.cards)


class Dealer(Player):
    def __init__(self, parent):
        super().__init__("Dealer", "NORTH", parent)
        self.deck = Deck()
        # self.hand = []
        # self.cardX = Player.seatLocation[self.seat][0]
        # self.cardY = Player.seatLocation[self.seat][1]

    def deal(self):
        return self.deck.next()

class MainFrame(BaseWindow):
    def buildWidgets(self):
        self.root.configure(bg='#00FFFF')
        self.boardFrame = PlayBoardFrame(self)
        self.configFrame = ConfigFrame(self)
        self.configFrame.pack(fill=BOTH, expand=1)
    
    def switchToBoardFrame(self):
        self.configFrame.hide()
        self.boardFrame.pack(fill=BOTH, expand=1)

    def switchToConfigFrame(self):
        self.boardFrame.hide()
        self.configFrame.pack(fill=BOTH, expand=1)

    def updatePlayerName(self, seat, name):
        self.boardFrame.updatePlayerName(seat, name)

    def setBackground(self, color):
        self.boardFrame.setBackground(color)

class ConfigFrame():
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent.root, bg='#568568')
        welcomeLbl = Label(self.frame, text='Welcome to Our Blackjack Game!', bg='#568568', fg='#630A4A', font=('Arial Bold', 30)) #RGB in Hex
        welcomeLbl.pack(pady=30)
        # mainImage = PhotoImage(file='src/images/animation.gif')
        # imageLbl = Label(self.frame)
        # imageLbl.configure(image=mainImage)
        # imageLbl.image = mainImage
        imageLbl = ImageLabel(self.frame)
        imageLbl.load('images/animation.gif')
        imageLbl.pack()

        buttonFrm = Frame(self.frame)
        playerBtn = Button(buttonFrm, text="Config Player", command=self.popupSetSeat, bg='#e7b174')
        playerBtn.grid(row=0, column=0)
        bgBtn = Button(buttonFrm, text="Config Background", command=self.popupCofigBackground, bg='#e7b174')
        bgBtn.grid(row=0, column=1)
        startBtn = Button(buttonFrm, text="Start", width=27, bg='#630A4A', fg='white', command=self.switch)
        startBtn.grid(row=1, column=0, columnspan=2)

        buttonFrm.pack(pady=10)

    def pack(self, **kwargs):
        self.frame.pack(kwargs)

    def hide(self):
        self.frame.pack_forget() # this built in function get ride of this frame

    def switch(self):
        self.parent.switchToBoardFrame()

    def popupSetSeat(self):
        top = Toplevel(self.frame)
        rootX = self.frame.winfo_rootx()+350
        rootY = self.frame.winfo_rooty()+200
        top.geometry(f'250x150+{rootX}+{rootY}')
        top.title("set player's seat")
        bg='#568568'
        top.configure(bg=bg)
        Label(top, text="Player name:",bg=bg).grid(row=0,column=0, pady=10)
        self.nameEntry = Entry(top, width=23)
        self.nameEntry.grid(row=0, column=1, pady=10)
        self.playerNameVar = StringVar()
        self.playerNameVar.set("EAST")
        Label(top, text="Available Seats:",bg=bg).grid(row=1, column=0)
        self.combobox = Combobox(top,textvariable=self.playerNameVar,values=["EAST","SOUTH","WEST"])
        self.combobox.grid(row=1, column=1)
        setBtn = Button(top, text="Set", width=20, command=self.setPlayerSeat)
        setBtn.place(x=60, y=120)

    def closewin(self):
        pass

    def setPlayerSeat(self):
        self.parent.updatePlayerName(self.combobox.get(),self.nameEntry.get())

    def popupCofigBackground(self):
        top = Toplevel(self.frame)
        rootX = self.frame.winfo_rootx() + 350
        rootY = self.frame.winfo_rooty() + 200
        top.geometry(f'255x180+{rootX}+{rootY}') # 300,250 is width,height; 200,200 is topleft
        top.title("Set Background")
        bg='#568568'
        top.configure(bg=bg)
        self.colorVar = StringVar()
        self.colorVar.set('#FFFF00')
        precolors = [
            ("blue", '#0000FF'),
            ("red", '#FF0000'),
            ("yellow", '#FFFF00'),
            ("cyan", '#00FFFF'),
            ("gray", "#888888")
        ]
        frame = Frame(top,bg=bg)
        frame.pack()
        for text, color in precolors:
            b = Radiobutton(frame, text=text, variable=self.colorVar, value=color, bg=bg)
            b.pack(anchor=W)
        setBtn = Button(top, text="Set", width=20, command=self.setBackground)
        setBtn.pack()

    def setBackground(self):
        self.parent.setBackground(self.colorVar.get())

class PlayBoardFrame():
    def __init__(self, parent):
        self.index = 0
        self.parent = parent
        self.frame = Frame(parent.root, bg='#90F3C5')

        self.frame.cardLbls = []
        self.dealer = Dealer(self.frame)
        self.dealBtn = Button(self.frame, text="Deal Card", command=self.deal)
        self.dealBtn.place(x=10, y=0)
        self.configBtn = Button(self.frame, text="Config", command=self.switch)
        self.configBtn.place(x=80, y=0)
        self.updateBtn = Button(self.frame, text="Update Results", command=self.update)
        self.updateBtn.place(x=130, y=0)
        self.clearBtn = Button(self.frame, text="Clear", command=self.clear)
        self.clearBtn.place(x=220, y=0)
        self.exitBtn = Button(self.frame, text="Exit", command=self.exit)
        self.exitBtn.place(x=260, y=0)
        Label(self.frame,text="Player Name:").place(x=700, y=0)
        self.nameVar = StringVar()
        self.nameVar.set("East")
        self.playerName = Label(self.frame, textvariable=self.nameVar)
        self.playerName.place(x=780, y=0)
        self.hitBtn = Button(self.frame, text="Hit", command=self.hit)
        self.hitBtn.place(x=850, y=0)
        self.passBtn = Button(self.frame, text="Pass", command=self.pass_)
        self.passBtn.place(x=880, y=0)
        self.nameLbls = dict()
        setButtonEnabled(self.hitBtn, False)
        setButtonEnabled(self.passBtn, False)
        setButtonEnabled(self.clearBtn, False)
        setButtonEnabled(self.updateBtn, False)

        self.buildPlayerList()
        self.displayPlayerNames()
        self.buildResultFrame(self.frame)
        
    def append(self, cardLbl):
        self.frame.cardLbls.append(cardLbl)

    def buildResultFrame(self, screen):
        labelframe = LabelFrame(screen, text = "Game Result", bg=('#FFFF00'), width=300)
        for index in range(len(self.playerList)):
            player = self.playerList[index]
            player.nameLbl = Label(labelframe, textvariable=player.nameVar, bg=('#FFFF00'))
            player.winLbl = Label(labelframe, textvariable=player.winVar, bg=('#FFFF00'))
            player.nameLbl.grid(row=index, column=0)
            player.winLbl.grid(row=index, column=1)
        labelframe.place(x=800, y=60, width=150, height=120)

    def deal(self):
        player = self.playerList[self.index]
        player.addCardToHand(self.dealer.deal())
        self.index += 1
        if self.index > 3:
            self.index = 0
        if player.name=="Dealer" and len(player.hand)==2: # disable deal button
            setButtonEnabled(self.dealBtn, False)
            setButtonEnabled(self.hitBtn, True)
            setButtonEnabled(self.passBtn, True)
        player = self.playerList[self.index]
        self.nameVar.set(player.name)

            
    def update(self):
        dealerTotal = self.dealer.getHandValue()
        for index in range(3):
            player = self.playerList[index]
            playerTotal = player.getHandValue()
            if playerTotal>21:
                self.dealer.win()
            elif dealerTotal>21:
                player.win()
            elif dealerTotal==playerTotal:
                pass
            elif dealerTotal > playerTotal:
                self.dealer.win()
            else:
                player.win()
        # for player in self.playerList:
        #     print(f"{player.name}:{player.winCount}")
        setButtonEnabled(self.updateBtn, False)
        self.updateResult()
        setButtonEnabled(self.clearBtn, True)

    def updateResult(self): # update game result on screen
        for player in self.playerList:
            player.updateWinCount()

    def clear(self):
        for cardLbl in self.frame.cardLbls: # clear all cards on screen
            cardLbl.destroy()
        self.frame.cardLbls.clear() # clear memory for avoid memory leak
        for player in self.playerList:
            player.clearHand() # clear all cards in hand
            player.cardX = Player.seatLocation[player.seat][0] # put card initial location back
        setButtonEnabled(self.clearBtn, False)
        setButtonEnabled(self.dealBtn, True)


    def exit(self):
        sys.exit()

    def hit(self):
        player = self.playerList[self.index]
        player.addCardToHand(self.dealer.deal())
        self.nameVar.set(player.name)

    def pass_(self):
        self.index += 1
        player = self.playerList[self.index]
        self.nameVar.set(player.name)
        if player.name=="Dealer":
            self.index = 0
            setButtonEnabled(self.hitBtn, False) # disable hit and pass buttons
            setButtonEnabled(self.passBtn, False)  
            self.frame.facedownLbl.destroy() # delete teh facedown card
            while self.dealer.getHandValue() < 17: # add more card to dealer if necessary
                self.dealer.addCardToHand(self.dealer.deal())
            setButtonEnabled(self.updateBtn, True) # it is time to find game result


    def displayPlayerNames(self):
        for player in self.playerList:
            lbl = Label(self.frame, text=player.name)
            lbl.place(x=player.getCardX()-70, y=player.getCardY())
            self.nameLbls[player.seat] = lbl


    def buildPlayerList(self):
        self.playerList = []
        player = Player("East", "EAST", self.frame)
        self.playerList.append(player)
        player = Player("South", "SOUTH", self.frame)
        self.playerList.append(player)
        player = Player("West", "WEST", self.frame)
        self.playerList.append(player)
        self.playerList.append(self.dealer)
        

    def pack(self, **kwargs):
        self.frame.pack(kwargs)

    def hide(self):
        self.frame.pack_forget() # this built in function get ride of this frame

    def switch(self):
        self.parent.switchToConfigFrame()

    def updatePlayerName(self, seat, name):
        for player in self.playerList:
            if player.seat == seat:
                player.name = name
        self.updateBoard()

    def updateBoard(self): # update all player's name on board
        for player in self.playerList:
            lbl = self.nameLbls[player.seat]
            lbl.configure(text=player.name)  
            player.nameVar.set(player.name)
        player = self.playerList[self.index]
        self.nameVar.set(player.name) # self.nameVar is the current player name label on topright cornor

    def setBackground(self, bg):
        self.frame.configure(bg=bg)

if __name__ == '__main__':
    MainFrame()