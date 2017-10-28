import sys

# pieces are what?
# an array of type piece

# board

# piece has an x,y coordinate and a type

class Board:
    def stringToArray(self):
        self.splitStrings = self.string.split('\n')

    def boardArrayToString(self):
        self.string = ''
        for i in range(len(self.splitStrings)):
            self.string += self.splitStrings[i]+'\n'
            
    def __init__(self, string_i = ''):
        if string_i == '':
            self.string = "rkbqkbkr\npppppppp\n........\n........\n........\n........\nPPPPPPPP\nRKBQKBKR"
        else:
            self.string = string_i
        self.splitString = self.stringToArray()
#\npppppppp\n........\n........\n........\n........\nPPPPPPPP\nRKBQKBKR"


# self.arr = [
        #     "rkbqkbkr",
        #     "pppppppp",
        #     "........",
        #     "........",
        #     "........",
        #     "........",
        #     "PPPPPPPP",                       
        #     "RKBQKBKR"
        # ]

    # this method doesn't work - using array directly
    def getPieceAtPoint(self, point):
        return self.string[point.y*8]

class Point:
    def __init__(self, xi, yi):
        self.x = xi
        self.y = yi

class Piece:
    def __init__(self, type_i, point_i):
        self.type = type_i
        self.point = point_i
        self.moved = False
        # self.history = []
        
def evaluatePawn(Piece):
    # is starting position?
    return None

def evaluateRook():
    return None

def evaluateKnight():
    return None

def evaluateBishop():
    # check all diagonals
    # check left diagonal forward
    # check right diagonal forward
    # check left diagonal backward
    # check right diagonal backward
    # return possible moves
    return None

def evaluateQueen():
    return None

def evaluateKing():
    return None

