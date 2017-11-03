import sys

# pieces are what?
# an array of type piece

# board

# piece has an x,y coordinate and a type


    # this method doesn't work - using array directly
#    def getPieceAtPoint(self, point):
#        return self.string[point.y*8]

# -------------------------
class Point:
    def __init__(self, xi, yi):
        self.x = xi
        self.y = yi

# -------------------------
class Piece:
    def __init__(self,
                 type_i='p',
                 color_i='n',
                 x_i = 0,
                 y_i = 0
    ):
        self.type = type_i
        self.color = color_i
        self.x = x_i
        self.y = y_i
        self.moved = False
        self.history = []
        
class Board:
    pieces = list()
#    pieces = ['p','p','p','p','p','p','p','p','r','n','b','q','k','b','n','r','P','P','P','P','P','P','P','P','R','N','B','Q','K','B','N','R']

# -------------------------
    # pawns are the soul of chess
    def evaluatePawn(self,pawn):        
        print('evaluating moves for '+str(pawn.color)+str(pawn.type)+' (' + str(pawn.x) +','+str(pawn.y) + ')')
        # make a dict: {pos: set(moves)}
        px = pawn.x
        py = pawn.y
        pcolor = pawn.color
        pos = str(px)+','+str(py) # should be a tuple?
        moves = set()
        ev = {pos:moves}
        m = 1
        # check edges
        if pcolor == 'w': # go backwards            
            m = -1
        # is starting position?        
        if not pawn.moved:         # check up 2
            print('can move 2')
            n = 2*m
            tx = px + n
            thisCell = self.splitStrings[tx][py]
            if thisCell == '.': 
                moves.add( str(tx) + ',' + str(py) )            
        # check forward 1
        tx = px + m
        thisCell = self.splitStrings[tx][py]
        if thisCell == '.':
            moves.add( str(tx) + ',' + str(py) )        
        # check left diagonal
        tx = px + m
        ty = py - 1
        thisCell = self.splitStrings[tx][ty]
        if thisCell != '.':
            moves.add( str(tx) + ',' + str(ty) )        
        ty = py + 1
        if thisCell != '.':
            moves.add( str(tx) + ',' + str(ty) )                    
        # check right diagonal
        # check en passant
        print(ev)
        return ev

# -------------------------    
    def evaluateRook(self,rook):
        print('evaluating moves for'+str(rook.color)+str(rook.type)+' (' + str(rook.x) +','+str(rook.y) + ')')
        px = rook.x
        py = rook.y
        pos = str(px)+','+str(py) # should be a tuple?
        moves = set()
        ev = {pos:moves}        
        # check up
        # - -----
        # - check for upper board edge
        i = 1        
        while px - i > 0 :
            print('px-i='+str(px-i))
            tx = px - i
            thisCell = self.splitStrings[tx][py]
            if thisCell == '.':
                moves.append( str(px-i) + ',' + str(py) )
            else:
                break
            i += 1
            print(moves)
            print('i='+str(i))
            print('\n')
        # - check for piece blocking
        # down
        # left
        # right
        return ev

# -------------------------
    def evaluateKnight(self,knight):
        print('evaluating moves for '+str(knight.color)+str(knight.type)+' (' + str(knight.x)  +','+str(knight.y) + ')')
        px = knight.x
        py = knight.y
        pos = str(px)+','+str(py) # should be a tuple?
        moves = set()
        ev = {pos:moves}                

        # check up 2  left 1
        # check top edge         # check left edge
        tx = px - 2
        ty = py - 1
        if tx >= 0 and ty >= 0: # check if square is empty or opposing
            if self.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty))
        # check right edge                # check bottom edge        

        # check up 2 right 1
        tx = px - 2
        ty = py + 1
        if tx >= 0 and ty <= 7: # check if square is empty or opposing
            if self.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty) )        
        # check left 2 up 1
        tx = px - 1
        ty = py - 2
        if tx >= 0 and ty >= 0: # check if square is empty or opposing
            if self.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty) )
        
        # check left 2 down 1
        tx = px + 1
        ty = py - 2
        if tx <= 7 and ty >= 0: # check if square is empty or opposing
            if self.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty) )
        
        # check right 2 up 1
        tx = px - 1
        ty = py + 2
        if tx >= 0 and ty <= 7: # check if square is empty or opposing
            if self.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty) )
        
        # check right 2 down 1
        tx = px + 1
        ty = py + 2
        if tx <= 7 and ty <= 7: # check if square is empty or opposing
            if self.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty) )
        
        # check down 2 left 1
        tx = px + 2
        ty = py - 1
        if tx <= 7 and ty >= 0: # check if square is empty or opposing
            if self.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty))
        
        # check down 2 right 1
        tx = px + 2
        ty = py + 1
        if tx <= 7 and ty <= 7: # check if square is empty or opposing
            if self.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty))
        print(ev)
        return ev

# -------------------------    
    def evaluateBishop(self,bishop):
    # check all diagonals
    # check left diagonal forward
    # check right diagonal forward
    # check left diagonal backward
    # check right diagonal backward
    # return possible moves
        return None

# -------------------------    
    def evaluateQueen(self,queen):
        return None

# -------------------------    
    def evaluateKing(self,king):
        return None

# -------------------------    
    def stringToArray(self):
        splitStrings = self.string.split('\n')
        self.splitStrings = []
        for i in range(len(splitStrings)):
            self.splitStrings.append(list(splitStrings[i]))
            
    def boardArrayToString(self):
        self.string = ''
        for i in range(len(self.splitStrings)):
            self.string += ''.join(self.splitStrings[i])+'\n'

    def piecesFromBoardStrings(self):
        ss = self.splitStrings
        self.pieces = list()
        for i in range(len(ss)):
            row = ss[i]
            print(row)
            for j in range(len(row)):
                #  print(ss[i][j])
                if not( ss[i][j] == '.' ):
                    color = 'b'
                    if ss[i][j].istitle():
                        color = 'w'
                    self.pieces.append( Piece( ss[i][j], color, i, j ) )

    def printPieces(self):
        for piece in self.pieces:
            pType = piece.type
            px = piece.x
            py = piece.y
            pcolor = piece.color
            print('type: '+pType+' color:'+pcolor+' x:'+str(px)+' y:'+str(py))

    # -------------------------
    def getAllPossibleMoves(self):
        moves = list()
        for piece in self.pieces:
            pType = piece.type
            px = piece.x
            py = piece.y
            pcolor = piece.color
            print('type: '+pType+' color:'+pcolor+' x:'+str(px)+' y:'+str(py))
            # pawn
            if pType.lower() == 'p':
                moves.append(self.evaluatePawn(piece))
            # rook
            if pType.lower() == 'r':
                moves.append(self.evaluateRook(piece))
            # knight
            if pType.lower() == 'n':
                moves.append(self.evaluateKnight(piece))
            # bishop
            if pType.lower() == 'b':
                self.evaluateBishop(piece)

            # queen
            if pType.lower() == 'q':
                self.evaluateQueen(piece)

            # king
            if pType.lower() == 'k':
                self.evaluateKing(piece)
            
        for move in moves:
            print(move)

    # -------------------------            
    def __init__(self, string_i = ''):
        if string_i == '':
            self.string = "rnbqkbnr\npppppppp\n........\n........\n........\n........\nPPPPPPPP\nRNBQKBNR"
        else:
            self.string = string_i
        self.splitString = self.stringToArray()

b1 = Board()
b1.piecesFromBoardStrings()
b1.getAllPossibleMoves()
