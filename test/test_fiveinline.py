import unittest
from src.fiveinline import *

class TestFiveInline(unittest.TestCase):

    def test_fiveInLineTrue(self):
        board = Board(None)
        board.chessPieces[2][3] = 'W'
        board.chessPieces[2][4] = 'W'
        board.chessPieces[2][5] = 'W'
        board.chessPieces[2][6] = 'W'
        board.chessPieces[2][7] = 'W'
        self.assertEquals((True,'W'), board.fiveInLine())

    def test_fiveInLineFalse(self):
        board = Board(None)
        board.chessPieces[0][3] = 'W'
        board.chessPieces[0][4] = 'W'
        board.chessPieces[0][5] = 'B'
        board.chessPieces[0][6] = 'W'
        board.chessPieces[0][7] = 'W'
        actual = board.fiveInLine()
        self.assertEquals((False,None), actual)
    
    def test_columnYes(self):
        board = Board(None)
        board.chessPieces[3][4] = 'W'
        board.chessPieces[4][4] = 'W'
        board.chessPieces[5][4] = 'W'
        board.chessPieces[6][4] = 'W'
        board.chessPieces[7][4] = 'W'
        self.assertEquals((True,'W'), board.fiveInLine())

    def test_columnEdgeYes(self):
        board = Board(None)
        board.chessPieces[10][14] = 'W'
        board.chessPieces[11][14] = 'W'
        board.chessPieces[12][14] = 'W'
        board.chessPieces[13][14] = 'W'
        board.chessPieces[14][14] = 'W'
        self.assertEquals((True,'W'), board.fiveInLine())

    def test_columnEdgeNo(self):
        board = Board(None)
        board.chessPieces[10][14] = 'W'
        board.chessPieces[11][14] = 'W'
        board.chessPieces[12][14] = 'W'
        board.chessPieces[13][14] = 'B'
        board.chessPieces[14][14] = 'W'
        self.assertEquals((False, None), board.fiveInLine())

    def test_columnNo(self):
        board = Board(None)
        board.chessPieces[3][4] = 'W'
        board.chessPieces[4][4] = 'B'
        board.chessPieces[5][4] = 'W'
        board.chessPieces[6][4] = 'W'
        board.chessPieces[7][4] = 'W'
        actual = board.fiveInLine()
        self.assertEquals((False,None), actual)

    def test_baskslashYes(self):
        board = Board(None)
        board.chessPieces[3][4] = 'W'
        board.chessPieces[4][5] = 'W'
        board.chessPieces[5][6] = 'W'
        board.chessPieces[6][7] = 'W'
        board.chessPieces[7][8] = 'W'
        self.assertEquals((True,'W'), board.fiveInLine())

    def test_baskslashNo(self):
        board = Board(None)
        board.chessPieces[3][4] = 'W'
        board.chessPieces[4][5] = 'W'
        board.chessPieces[5][6] = 'W'
        board.chessPieces[6][7] = 'B'
        board.chessPieces[7][8] = 'W'
        self.assertEquals((False,None), board.fiveInLine())

    def test_forwardslashYes(self):
        board = Board(None)
        board.chessPieces[14][0] = 'W'
        board.chessPieces[13][1] = 'W'
        board.chessPieces[12][2] = 'W'
        board.chessPieces[11][3] = 'W'
        board.chessPieces[10][4] = 'W'
        self.assertEquals((True,'W'), board.fiveInLine())

    def test_forwardslashNo(self):
        board = Board(None)
        board.chessPieces[14][0] = 'B'
        board.chessPieces[13][1] = 'W'
        board.chessPieces[12][2] = 'W'
        board.chessPieces[11][3] = 'W'
        board.chessPieces[10][4] = 'W'
        self.assertEquals((False,None), board.fiveInLine())

