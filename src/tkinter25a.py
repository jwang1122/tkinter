"""
using tkinter.Menu()
"""
from tkinterbase import *
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

class MenuWindow(TkinterBase):
    def buildWidget(self):
        self.menubar = Menu(self.root)
        self.buildFileMenu()
        self.root.config(menu = self.menubar)

    def buildFileMenu(self):
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.openNewFile)        
        filemenu.add_command(label="Open", command=self.openFile)
        filemenu.add_command(label="Save", command=self.saveFile)
        filemenu.add_command(label="Close", command=self.closeFile)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.exit)
        self.menubar.add_cascade(label="File", menu=filemenu)

    def buildEditMenu(self):
        # Cut, Copy, Paste, Delete, Select All
        pass

    def buildHelpMenu(self):
        # About, Help
        pass
    
    def openNewFile(self):
        pass

    def openFile(self):
        pass

    def saveFile(self):
        pass

    def closeFile(self):
        pass

    def exit(self):
        pass

if __name__ == '__main__':
    MenuWindow()