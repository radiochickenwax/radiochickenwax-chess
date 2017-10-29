import sys

# pieces are what?
# an array of type piece

# board

# piece has an x,y coordinate and a type


    # this method doesn't work - using array directly
#    def getPieceAtPoint(self, point):
#        return self.string[point.y*8]

class Point:
    def __init__(self, xi, yi):
        self.x = xi
        self.y = yi

class Piece:
    def __init__(self,
                 type_i='p',
                 color='n',
                 point_i=Point(0,0),                 
    ):
        self.type = type_i
        self.color = color_i
        self.point = point_i
        self.moved = False
        self.history = []
        
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

class Board:
    pieces = list()
#    pieces = ['p','p','p','p','p','p','p','p','r','n','b','q','k','b','n','r','P','P','P','P','P','P','P','P','R','N','B','Q','K','B','N','R']

    def stringToArray(self):
        splitStrings = self.string.split('\n')
        self.splitStrings = []
        for i in range(len(splitStrings)):
            self.splitStrings.append(list(splitStrings[i]))
            
    def boardArrayToString(self):
        self.string = ''
        for i in range(len(self.splitStrings)):
            self.string += ''.join(self.splitStrings[i])+'\n'

    def piecesFromBoardString(self):
        ss = self.splitStrings
        self.pieces = list()
        for i in range(len(ss)):
            row = ss[i]
            print(row)
            for j in range(len(row)):
                print(ss[i][j])
                if not( ss[i][j] == '.' ):
                    self.pieces.append( Piece( ss[i][j], Point(i,j) ) )
            
    def __init__(self, string_i = ''):
        if string_i == '':
            self.string = "rnbqkbnr\npppppppp\n........\n........\n........\n........\nPPPPPPPP\nRNBQKBNR"
        else:
            self.string = string_i
        self.splitString = self.stringToArray()
