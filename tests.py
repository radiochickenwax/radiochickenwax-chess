# initial board        
# b1 = Board()
# b1.piecesFromBoardStrings()
# b1.getAllPossibleMoves()

# TODO: generate board strings from pieces / moves
# TODO: rethink data structs

# -----------------------------------------------------------------------------
# TODO:   turn the tests below into valid unit tests (use pytest or something)
# -----------------------------------------------------------------------------

# TODO: test rooks possible moves
# print('emptyRook\n-------------\n')
# emptyRook = Board('........\n........\n...r....\n........\n........\n........\n........\n........')
# emptyRook.piecesFromBoardStrings()
# emptyRook.getAllPossibleMoves()

# TODO: test rook taking opposing piece
# print('rookPawn\n-------------\n')
# rookPawn = Board('........\n........\n...r..p.\n........\n........\n........\n...P....\n........')
# rookPawn.piecesFromBoardStrings()
# rookPawn.getAllPossibleMoves()

# TODO: test rook taking opposing piece

# TODO: test knights possible moves
# print('emptyKnight\n-------------\n')
# emptyKnight = Board('........\n........\n...n....\n........\n........\n........\n........\n........')
# emptyKnight.piecesFromBoardStrings()
# emptyKnight.getAllPossibleMoves()
-
# TODO: test bishops possible moves
# print('bishopPawn\n-------------\n')
# bishopPawn = Board('........\n........\n...b..p.\n........\n........\n........\n...P....\n........')
# bishopPawn.piecesFromBoardStrings()
# bishopPawn.getAllPossibleMoves()
-
# TODO: test kings possible moves
# print('emptyKing\n-------------\n')
# emptyKing = Board('........\n........\n...k....\n........\n........\n........\n........\n........')
# emptyKing.piecesFromBoardStrings()
# emptyKing.getAllPossibleMoves()
-
# TODO: test kings possible moves on borders
# print('emptyKing NW\n-------------\n')
# emptyKing = Board('k.......\n........\n........\n........\n........\n........\n........\n........')
# emptyKing.piecesFromBoardStrings()
# emptyKing.getAllPossibleMoves()
-
# print('emptyKing SE\n-------------\n')
# emptyKing = Board('........\n........\n........\n........\n........\n........\n........\n.......k')
# emptyKing.piecesFromBoardStrings()
# emptyKing.getAllPossibleMoves()
-
# print('emptyKing NE\n-------------\n')
# emptyKing = Board('.......k\n........\n........\n........\n........\n........\n........\n........')
# emptyKing.piecesFromBoardStrings()
# emptyKing.getAllPossibleMoves()
-
# print('emptyKing SW\n-------------\n')
# emptyKing = Board('........\n........\n........\n........\n........\n........\n........\nk.......')
# emptyKing.piecesFromBoardStrings()
# emptyKing.getAllPossibleMoves()
-
-print('kingPawn opposing\n-------------\n')
-kingPawn = Board('........\n........\n........\n........\n........\n........\n.P......\n.k......')
-kingPawn.piecesFromBoardStrings()
-kingPawn.getAllPossibleMoves()
-
-print('kingPawn friendly\n-------------\n')
-kingPawn = Board('........\n........\n........\n........\n........\n........\n.p......\n.k......')
-kingPawn.piecesFromBoardStrings()
-kingPawn.getAllPossibleMoves()
-
# TODO: test queens possible moves
# print('queenPawn\n-------------\n')
# queenPawn = Board('........\n........\n...q..p.\n........\n........\n........\n...P....\n........')
# queenPawn.piecesFromBoardStrings()
# queenPawn.getAllPossibleMoves()
-
# TODO: test if move is check
# TODO: test if move is mate
-
# TODO: test pawn move - should generate new board
# TODO: test pawn captures - should generate new board
-
# TODO: test queen move
# TODO: test queen captures
