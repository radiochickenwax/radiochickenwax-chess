import sys
import pprint
# pieces are what?
# an array of type piece

# board

# piece has an x,y coordinate and a type


    # this method doesn't work - using array directly
#    def getPieceAtPoint(board, point):
#        return board.string[point.y*8]

# -------------------------
class Point:
    def __init__(board, xi, yi):
        board.x = xi
        board.y = yi

# -------------------------
class Piece:
    def __init__(board,
                 type_i='p',
                 color_i='n',
                 x_i = 0,
                 y_i = 0
    ):
        board.type = type_i
        board.color = color_i
        board.x = x_i
        board.y = y_i
        board.moved = False
        board.history = []


class Board:
    '''
    The board has pieces, and can generate sets of possible moves.
    '''
    pieces = list() # these are parsed from the init string in piecesFromBoardStrings()
    pieceCoordinates = dict()
    moves = dict()
    wMoves = dict()
    bMoves = dict()        
    turns = {'w':'','b':''}
    currentTurn = 'w'    
    pprinter = pprint.PrettyPrinter(indent=4)
    # -------------------------            
    def __init__(board, string_i = ''):
        #pprinter = pprint.PrettyPrinter(indent=4)
        if string_i == '':
            board.string = "rnbqkbnr\npppppppp\n........\n........\n........\n........\nPPPPPPPP\nRNBQKBNR"
        else:
            board.string = string_i
        board.splitString = board.stringToArray()
        board.piecesFromBoardStrings()          # generate pieces 
        board.getAllPossibleMoves()             # generate moves

    # -------------------------            
    def getPieceOnSquare(board, x_i, y_i):
        # print('searching for piece on ' + str(x_i)+','+str(y_i) )
        thisPiece = None
        for piece in board.pieces:
            # print(piece.type+' tpcolor:'+str(piece.color)+' tpx:'+str(piece.x)+' tpy:'+str(piece.y))
            if piece.x == x_i and piece.y == y_i:
                thisPiece = piece
                break
        return thisPiece

# -------------------------
    # pawns are the soul of chess
    def evaluatePawn(board,pawn):        
        # print('evaluating moves for '+str(pawn.color)+str(pawn.type)+' (' + str(pawn.x) +','+str(pawn.y) + ')')
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
        if (pcolor == 'b' and px == 1) or (pcolor == 'w' and px == 6):
            #print('can move 2')
            n = 2*m
            tx = px + n
            thisCell = board.splitStrings[tx][py]
            if thisCell == '.': 
                moves.add( str(tx) + ',' + str(py) )            
        # check forward 1
        tx = px + m
        thisCell = board.splitStrings[tx][py]
        if thisCell == '.':
            moves.add( str(tx) + ',' + str(py) )        
        # check left diagonal
        tx = px + m
        ty = py - 1
        thisCell = board.splitStrings[tx][ty]
        if thisCell != '.':
            moves.add( str(tx) + ',' + str(ty) )        
        ty = py + 1
        if thisCell != '.':
            moves.add( str(tx) + ',' + str(ty) )                    
        # check right diagonal
        # check en passant
        # print(ev)
        return ev

# -------------------------    
    def evaluateRook(board,rook):
        # print('evaluating moves for'+str(rook.color)+str(rook.type)+' (' + str(rook.x) +','+str(rook.y) + ')')
        px = rook.x
        py = rook.y
        pcolor = rook.color
        pos = str(px)+','+str(py) # should be a tuple?
        moves = set()
        ev = {pos:moves}        
        # check up
        # - -----
        # - check for upper board edge
        i = 1        
        while px - i >= 0:         # - check for piece blocking
            tx = px - i
            thisCell = board.splitStrings[tx][py]
            if thisCell == '.': # or opposing piece
                moves.add( str(px-i) + ',' + str(py) )
            else:
                # if # is opposing piece
                thisPiece = board.getPieceOnSquare(tx,py)
                if thisPiece.color != rook.color:
                    moves.add( str(tx) + ',' + str(py) )
                break
            i += 1
        # down
        i = -1        
        while px - i <= 7 :
            tx = px - i
            thisCell = board.splitStrings[tx][py]
            if thisCell == '.':
                moves.add( str(px-i) + ',' + str(py) )
            else:
                thisPiece = board.getPieceOnSquare(tx,py)                
                if thisPiece.color != rook.color:
                    moves.add( str(tx) + ',' + str(py) )
                break
            i -= 1        
        # left
        i = 1        
        while py - i >= 0 :
            ty = py - i
            thisCell = board.splitStrings[px][ty]
            if thisCell == '.':
                moves.add( str(px) + ',' + str(ty) )
            else:
                thisPiece = board.getPieceOnSquare(px,ty)                
                if thisPiece.color != rook.color:
                    moves.add( str(px) + ',' + str(ty) )
                break
            i += 1        
        # right
        i = 1        
        while py + i <= 7 :
            ty = py + i
            thisCell = board.splitStrings[px][ty]
            if thisCell == '.':
                moves.add( str(px) + ',' + str(ty) )
            else:
                thisPiece = board.getPieceOnSquare(px,ty)
                if thisPiece.color != rook.color:
                    moves.add( str(px) + ',' + str(ty) )
                break
            i += 1        
        return ev

# -------------------------
    def evaluateKnight(board,knight):
        # print('evaluating moves for '+str(knight.color)+str(knight.type)+' (' + str(knight.x)  +','+str(knight.y) + ')')
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
            if board.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty))
        # check right edge                # check bottom edge        

        # check up 2 right 1
        tx = px - 2
        ty = py + 1
        if tx >= 0 and ty <= 7: # check if square is empty or opposing
            if board.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty) )        
        # check left 2 up 1
        tx = px - 1
        ty = py - 2
        if tx >= 0 and ty >= 0: # check if square is empty or opposing
            if board.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty) )
        
        # check left 2 down 1
        tx = px + 1
        ty = py - 2
        if tx <= 7 and ty >= 0: # check if square is empty or opposing
            if board.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty) )
        
        # check right 2 up 1
        tx = px - 1
        ty = py + 2
        if tx >= 0 and ty <= 7: # check if square is empty or opposing
            if board.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty) )
        
        # check right 2 down 1
        tx = px + 1
        ty = py + 2
        if tx <= 7 and ty <= 7: # check if square is empty or opposing
            if board.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty) )
        
        # check down 2 left 1
        tx = px + 2
        ty = py - 1
        if tx <= 7 and ty >= 0: # check if square is empty or opposing
            if board.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty))
        
        # check down 2 right 1
        tx = px + 2
        ty = py + 1
        if tx <= 7 and ty <= 7: # check if square is empty or opposing
            if board.splitStrings[tx][ty] == '.': # or opposing
                moves.add( str(tx) + ',' + str(ty))
        # print(ev)
        return ev

# -------------------------    
    def evaluateBishop(board,bishop):
        # print('evaluating moves for '+str(bishop.color)+str(bishop.type)+' (' + str(bishop.x)  +','+str(bishop.y) + ')')
        px = bishop.x
        py = bishop.y
        pos = str(px)+','+str(py) # should be a tuple?
        moves = set()
        ev = {pos:moves}                
        # check all diagonals
        # check left diagonal up
        i = 1
        while px - i >= 0 and py - i >= 0 :         # - check for piece blocking
            tx = px - i
            ty = py - i
            #print('tx:'+str(tx)+', ty:'+str(ty)+' moves:'+str(ev))
            thisCell = board.splitStrings[tx][ty]
            if thisCell == '.':
                moves.add( str(tx) + ',' + str(ty))
            else:
                thisPiece  = board.getPieceOnSquare(tx,ty)
                if thisPiece.color != bishop.color:
                    moves.add( str(tx) + ',' + str(ty) )
                break
            i+=1
        # check right diagonal up
        i = 1
        while px - i >= 0 and py + i <= 7 :         # - check for piece blocking
            tx = px - i
            ty = py + i
            #print('tx:'+str(tx)+', ty:'+str(ty)+' moves:'+str(ev))
            thisCell = board.splitStrings[tx][ty]
            if thisCell == '.':
                moves.add( str(tx) + ',' + str(ty))
            else:
                thisPiece  = board.getPieceOnSquare(tx,ty)
                if thisPiece.color != bishop.color:
                    moves.add( str(tx) + ',' + str(ty) )
                break
            i+=1
        # check left diagonal down
        i = 1
        while px + i <= 7 and py - i >= 0 :         # - check for piece blocking
            tx = px + i
            ty = py - i
            #print('tx:'+str(tx)+', ty:'+str(ty)+' moves:'+str(ev))
            thisCell = board.splitStrings[tx][ty]
            if thisCell == '.':
                moves.add( str(tx) + ',' + str(ty))
            else:
                thisPiece  = board.getPieceOnSquare(tx,ty)
                if thisPiece.color != bishop.color:
                    moves.add( str(tx) + ',' + str(ty) )
                break
            i+=1
        # check right diagonal down
        i = 1
        while px + i <= 7 and py + i <= 7 :         # - check for piece blocking
            tx = px + i
            ty = py + i
            #print('tx:'+str(tx)+', ty:'+str(ty)+' moves:'+str(ev))
            thisCell = board.splitStrings[tx][ty]
            if thisCell == '.':
                moves.add( str(tx) + ',' + str(ty))
            else:
                thisPiece  = board.getPieceOnSquare(tx,ty)
                if thisPiece.color != bishop.color:
                    moves.add( str(tx) + ',' + str(ty) )
                break
            i+=1
        # return possible moves
        return ev

# -------------------------    
    def evaluateQueen(board,queen):
        # print('evaluating moves for '+str(queen.color)+str(queen.type)+' (' + str(queen.x)  +','+str(queen.y) + ')')
        px = queen.x
        py = queen.y
        pos = str(px)+','+str(py) # should be a tuple?
        bishopStyleMoves = board.evaluateBishop(queen)[pos]
        rookStyleMoves = board.evaluateRook(queen)[pos]
        ev = {pos: bishopStyleMoves | rookStyleMoves}
        return ev

# -------------------------    
    def evaluateKing(board,king):
        # print('evaluating moves for '+str(king.color)+str(king.type)+' (' + str(king.x)  +','+str(king.y) + ')')
        px = king.x
        py = king.y
        pos = str(px)+','+str(py) # should be a tuple?
        moves = set()
        ev = {pos:moves}                
        # check px-1, py (north)
        if px - 1 >= 0:
            # print('checking north')
            tx = px-1
            ty = py
            thisCell = board.splitStrings[tx][ty]
            if thisCell == '.':
                moves.add( str(tx) + ',' + str(ty))
            else:
                thisPiece  = board.getPieceOnSquare(tx,ty)
                if thisPiece.color != king.color:
                    moves.add( str(tx) + ',' + str(ty) )            
        # check px-1, py+1 (northeast)
        if px - 1 >= 0  and  py + 1 <= 7:
            # print('checking northeast')
            tx = px-1
            ty = py+1
            thisCell = board.splitStrings[tx][ty]
            if thisCell == '.':
                moves.add( str(tx) + ',' + str(ty))
            else:
                thisPiece  = board.getPieceOnSquare(tx,ty)
                if thisPiece.color != king.color:
                    moves.add( str(tx) + ',' + str(ty) )            
        # check px, py+1 (east)
        if py+1 <= 7:
            #print('checking east')
            tx = px
            ty = py+1
            thisCell = board.splitStrings[tx][ty]
            if thisCell == '.':
                moves.add( str(tx) + ',' + str(ty))
            else:
                thisPiece  = board.getPieceOnSquare(tx,ty)
                if thisPiece.color != king.color:
                    moves.add( str(tx) + ',' + str(ty) )            
        # check px+1, py+1 (southeast)
        if px+1 <= 7 and py+1 <=7:
            #print('checking southeast')
            tx = px+1
            ty = py+1
            thisCell = board.splitStrings[tx][ty]
            if thisCell == '.':
                moves.add( str(tx) + ',' + str(ty))
            else:
                thisPiece  = board.getPieceOnSquare(tx,ty)
                if thisPiece.color != king.color:
                    moves.add( str(tx) + ',' + str(ty) )            
        # check px+1, py(south)
        if px + 1 <= 7:
            # print('checking south')
            tx = px+1
            ty = py
            thisCell = board.splitStrings[tx][ty]
            if thisCell == '.':
                moves.add( str(tx) + ',' + str(ty))
            else:
                thisPiece  = board.getPieceOnSquare(tx,ty)
                if thisPiece.color != king.color:
                    moves.add( str(tx) + ',' + str(ty) )            
        # check px+1, py-1 (southwest)
        if px+1 <= 7 and py-1 >=0:
            # print('checking southwest')
            tx = px+1
            ty = py-1
            thisCell = board.splitStrings[tx][ty]
            if thisCell == '.':
                moves.add( str(tx) + ',' + str(ty))
            else:
                thisPiece  = board.getPieceOnSquare(tx,ty)
                if thisPiece.color != king.color:
                    moves.add( str(tx) + ',' + str(ty) )            
        # check px, py-1 (west)
        if py-1 >= 0:
            # print('checking west')
            tx = px
            ty = py-1
            thisCell = board.splitStrings[tx][ty]
            if thisCell == '.':
                moves.add( str(tx) + ',' + str(ty))
            else:
                thisPiece  = board.getPieceOnSquare(tx,ty)
                if thisPiece.color != king.color:
                    moves.add( str(tx) + ',' + str(ty) )            
        # check px-1, py-1 (northwest)
        if px-1 >=0 and py-1 >= 0:
            # print('checking northwest')
            tx = px-1
            ty = py-1
            thisCell = board.splitStrings[tx][ty]
            if thisCell == '.':
                moves.add( str(tx) + ',' + str(ty))
            else:
                thisPiece  = board.getPieceOnSquare(tx,ty)
                if thisPiece.color != king.color:
                    moves.add( str(tx) + ',' + str(ty) )            
        return ev

# -------------------------    
    def stringToArray(board):
        splitStrings = board.string.split('\n')
        board.splitStrings = []
        for i in range(len(splitStrings)):
            board.splitStrings.append(list(splitStrings[i]))
            
# -------------------------    
    def boardArrayToString(board):
        board.string = ''
        for i in range(len(board.splitStrings)):
            board.string += ''.join(board.splitStrings[i])+'\n'

# -------------------------    
    def piecesFromBoardStrings(board):
        ss = board.splitStrings
        board.pieces = list()
        for i in range(len(ss)):
            row = ss[i]
            print(row)
            for j in range(len(row)):
                #  print(ss[i][j])
                if not( ss[i][j] == '.' ):
                    color = 'b'
                    if ss[i][j].istitle():
                        color = 'w'
                    board.pieces.append( Piece( ss[i][j], color, i, j ) )

# -------------------------    
    def printPieces(board):
        for piece in board.pieces:
            pType = piece.type
            px = piece.x
            py = piece.y
            pcolor = piece.color
            # print('type: '+pType+' color:'+pcolor+' x:'+str(px)+' y:'+str(py))

# -------------------------
    def getAllPossibleMoves(board):
        for piece in board.pieces:
            pType = piece.type
            px = piece.x
            py = piece.y
            pcolor = piece.color
            board.pieceCoordinates[str(px)+','+str(py)] = piece
            # print('type: '+pType+' color:'+pcolor+' x:'+str(px)+' y:'+str(py))
            # pawn
            if pType.lower() == 'p':
                pawnMoves = board.evaluatePawn(piece)
                if pcolor == 'w':
                    board.wMoves.update(pawnMoves)
                if pcolor == 'b':
                    board.bMoves.update(pawnMoves)                    
                board.moves.update(pawnMoves)
            # rook
            if pType.lower() == 'r':
                rookMoves = board.evaluateRook(piece)                
                if pcolor == 'w':
                    board.wMoves.update(rookMoves)
                if pcolor == 'b':
                    board.bMoves.update(rookMoves)                    
                board.moves.update(rookMoves)
            # knight
            if pType.lower() == 'n':
                knightMoves = board.evaluateKnight(piece)                                
                if pcolor == 'w':
                    board.wMoves.update(knightMoves)
                if pcolor == 'b':
                    board.bMoves.update(knightMoves)                    
                board.moves.update(knightMoves)
            # bishop
            if pType.lower() == 'b':
                bishopMoves = board.evaluateBishop(piece)                                
                if pcolor == 'w':
                    board.wMoves.update(bishopMoves)
                if pcolor == 'b':
                    board.bMoves.update(bishopMoves)                    
                board.moves.update(bishopMoves)
            # queen
            if pType.lower() == 'q':
                queenMoves = board.evaluateQueen(piece)                                
                if pcolor == 'w':
                    board.wMoves.update(queenMoves)
                if pcolor == 'b':
                    board.bMoves.update(queenMoves)                    
                board.moves.update(queenMoves)                
            # king
            if pType.lower() == 'k':
                kingMoves = board.evaluateKing(piece)                                
                if pcolor == 'w':
                    board.wMoves.update(kingMoves)
                if pcolor == 'b':
                    board.bMoves.update(kingMoves)                    
                board.moves.update(kingMoves)
        #for move in moves:
        #    print(move)
        board.pprinter.pprint(board.moves)
        #board.moves = moves

# -------------------------    
    def filterMovesByColor(board,color):
        '''
        Return only the moves available for the given color
        '''
        for move in board.moves:
            #pp.pprint(move)]
            print('-----------\n'+str(move))
            print(board.moves[move])
            print('-----------')
        #board.moves = moves

# -------------------------    
    def possibleChecks(board):
        return None

# -------------------------    
    def move(board, startEnd):
        '''
        Process a move.  
        A move is a starting point and an ending point. (startEnd).
        It should be (a-h)(1-8) : (a-h)(1-8) - but not using that notation yet.
        If it is valid, alter the board to suit.  If it is invalid return the string "invalid".
        '''
        #print('moving')
        print(board.string)
        startEndSplit = startEnd.split(',')
        if len(startEndSplit) != 4:
            print('wrong number of args')
            return None
        # get first coordinate        
        sx_sy = str(startEndSplit[0])+','+str(startEndSplit[1])
        print('got starting position: '+sx_sy)
        turn = board.currentTurn

        # verify sx_sy is correct turn piece (color)
        # need to get piece from coordinate

        pieceToMove = None
        if sx_sy in list(board.pieceCoordinates.keys()):
            pieceToMove = board.pieceCoordinates[sx_sy]
            if pieceToMove.color == turn: # we're ok
                # get 2nd coordinate
                ex_ey = str(startEndSplit[2])+','+str(startEndSplit[3])
                print('got ending position: '+ex_ey)
                # get all possible moves
                board.piecesFromBoardStrings()  # generate split strings
                board.getAllPossibleMoves()     # generate possible moves
                if sx_sy in list(board.moves.keys()):
                    setOfMoves = board.moves[sx_sy]
                    if ex_ey in setOfMoves:
                        if ex_ey in list(board.pieceCoordinates.keys()):
                            pieceToCapture = board.pieceCoordinates[ex_ey]
                            if pieceToCapture.color != turn:
                                # capture pieceToCapture (remove from board.pieces)
                                del board.pieces[ex_ey]
                                # set coord for pieceToMove to ex_ey
                                # set square for sx_sy to '.'
                                # regenerate boards with new positions
                        else: # endpos is empty therefore valid
                            # set coord for pieceToMove to ex_ey
                            # set square for pieceToMove to '.'
                            # regenerate boards with new positions                            
                        return True
                #validMoves = list(
        # filter checks - if the king is in check, don't get all possible moves, only moves that remove the check        
        # if the move is in the possible moves list, alter the board split strings
        # alter the board string to match the split strings
        
        return False
    
# -------------------------    



class Game:
    '''
    A Game has two players who each take turns. 
    A Game has at least one Board.
    A Game has turns.  (A turn is a move).
    A Game has a winner.
    A Game prompts for a move and turns after each move.
    A Game checks if it is over.  
    A Game is over if a king is mated.
    A king is mated if it is in check and cannot get out of check.
    A king is in check if an opposing color can capture it on the next move.
    The Board should tell us if a king is in check.
    '''        
    board = Board()
    def __init__(game, string_i = ''):
        if string_i == '':
            print('Setting default board.')
            board = Board()
        else:
            print('Setting custom board.')
            board = Board(string_i)
        board.splitString = board.stringToArray()
