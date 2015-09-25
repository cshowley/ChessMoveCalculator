

"""Import the value of every square of a chess board into a dictionary, where the
    value of each dictionary key is the piece occupying that square. Positions are 
    broken down into x,y Cartesian coordinates with the origin at the lower left 
    corner of the board i.e. x,y = (0,0) at A:1
"""


# Generalized class for a piece that describes that piece's x/y coordinates on the
# board and whether that piece is white or black
class Piece(object):
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    def getRow(self):
        return self.y
    def getColumn(self):
        return self.x
    def getPosition(self):
        return self.x,self.y
    def setPosition(self,x0,y0):
        self.x = x0
        self.y = y0
    def getColor(self):
        return self.color


# The following classes describe the parameters in which each piece can move
class Pawn(Piece):
    def moveForwardOne(self):
        if self.color == 'white':
            return self.x,(self.y+1)
        elif self.color == 'black':
            return self.x,(self.y-1)
    def moveForwardTwo(self):
        if self.color == 'white':
            return self.x,(self.y+2)
        elif self.color == 'black':
            return self.x,(self.y-2)
    def captureLeft(self):
        if self.color == 'white':
            return (self.x-1),(self.y+1)
        # Black captures left from perspective of black player
        if self.color == 'black':
            return (self.x+1),(self.y-1)
    def captureRight(self):
        if self.color == 'white':
            return (self.x+1),(self.y+1)
        # Black captures right from perspective of black player
        if self.color == 'black':
            return (self.x-1),(self.y-1)


class Knight(Piece):
    def moveLeftUp(self):
        return (self.x-1),(self.y+2)
    def moveLeftDown(self):
        return (self.x-1),(self.y-2)
    def moveRightUp(self):
        return (self.x+1),(self.y+2)
    def moveRightDown(self):
        return (self.x+1),(self.y-2)
    def moveUpLeft(self):
        return (self.x-2),(self.y+1)
    def moveUpRight(self):
        return (self.x+2),(self.y+1)
    def moveDownLeft(self):
        return (self.x-2),(self.y-1)
    def moveDownRight(self):
        return (self.x+2),(self.y-1)


class Bishop(Piece):
    def diagUpLeft(self):
        self.x -= 1
        self.y += 1
        return self.x,self.y
    def diagUpRight(self):
        self.x += 1
        self.y += 1
        return self.x,self.y
    def diagDownLeft(self):
        self.x -= 1
        self.y -= 1
        return self.x,self.y
    def diagDownRight(self):
        self.x += 1
        self.y -= 1
        return self.x,self.y


class Queen(Piece):
    def moveUp(self):
        self.y += 1
        return self.x,self.y
    def moveDown(self):
        self.y -= 1
        return self.x,self.y
    def moveLeft(self):
        self.x -= 1
        return self.x,self.y
    def moveRight(self):
        self.x += 1
        return self.x,self.y
    def diagUpLeft(self):
        self.x -= 1
        self.y += 1
        return self.x,self.y
    def diagUpRight(self):
        self.x += 1
        self.y += 1
        return self.x,self.y
    def diagDownLeft(self):
        self.x -= 1
        self.y -= 1
        return self.x,self.y
    def diagDownRight(self):
        self.x += 1
        self.y -= 1
        return self.x,self.y


class King(Piece):
    def moveUp(self):
        return self.x,(self.y+1)
    def moveDown(self):
        return self.x,(self.y-1)
    def moveLeft(self):
        return (self.x-1),self.y
    def moveRight(self):
        return (self.x+1),self.y
    def diagUpLeft(self):
        return (self.x-1),(self.y+1)
    def diagUpRight(self):
        return (self.x+1),(self.y+1)
    def diagDownLeft(self):
        return (self.x-1),(self.y-1)
    def diagDownRight(self):
        return (self.x+1),(self.y-1)


class Rook(Piece):
    def moveUp(self):
        self.y += 1
        return self.x,self.y
    def moveDown(self):
        self.y -= 1
        return self.x,self.y
    def moveLeft(self):
        self.x -= 1
        return self.x,self.y
    def moveRight(self):
        self.x += 1
        return self.x,self.y


# Convert standard chess coordinates to x,y coordinates, where 0 <= x,y <= 7
def chessCoordToCartesian(char,num):
    if char == 'A':
        char = 0
    elif char == 'B':
        char = 1
    elif char == 'C':
        char = 2
    elif char == 'D':
        char = 3
    elif char == 'E':
        char = 4
    elif char == 'F':
        char = 5
    elif char == 'G':
        char = 6
    elif char == 'H':
        char = 7
    num -= 1
    return char,num


# Convert x,y coordinates back to chess coordinates
def cartesianToChessCoord(num1,num2):
    if num1 == 0:
        num1 = 'A'
    elif num1 == 1:
        num1 = 'B'
    elif num1 == 2:
        num1 = 'C'
    elif num1 == 3:
        num1 = 'D'
    elif num1 == 4:
        num1 = 'E'
    elif num1 == 5:
        num1 = 'F'
    elif num1 == 6:
        num1 = 'G'
    elif num1 == 7:
        num1 = 'H'
    num2 += 1
    return num1,num2


# Determine which class to assign a piece to depending on its name
def getPieceID(x,y,name,color,pieceType):
    if name == pieceType[0]:
        piece = Pawn(x,y,color)
    elif name == pieceType[1]:
        piece = Knight(x,y,color)
    elif name == pieceType[2]:
        piece = Bishop(x,y,color)
    elif name == pieceType[3]:
        piece = Queen(x,y,color)
    elif name == pieceType[4]:
        piece = King(x,y,color)
    elif name == pieceType[5]:
        piece = Rook(x,y,color)
    else:
        pass
    return piece


# For creating dictionary keys in chess coordinates
def keyGenerator(a,b):
    key = '%s' % a +':'+ '%s' % b
    return key


# State one possible move a piece can make and append to a list
def moveWriter(possibleMoves,name,square,key):
    possibleMoves.append('%s at <%s> can move to <%s>' % (name,square,key))
    return possibleMoves


# If a piece captures another piece, append move to the list
def captureWriter(possibleMoves,name,square,opponent,key):
    possibleMoves.append('%s at <%s> can capture %s at <%s>' %
                         (name,square,opponent,key))
    return possibleMoves


# The script starts below...
color = raw_input("Which player's turn is it (white/black)? ")
if color == 'white':
    opponent = 'black'
else:
    opponent = 'white'
filename = raw_input("What's the initial conditions' file name? ")
chessBoard = {}
columns = ['A','B','C','D','E','F','G','H']
rows = [1,2,3,4,5,6,7,8]

# Create a dictionary where each dictionary key corresponds to a square (64 keys)
for i in columns:
    for j in rows:
        key = keyGenerator(i,j)
        chessBoard[key] = [chessCoordToCartesian(i,j), None, None]

with open(filename,'r') as f:
    for line in f:
        line = line.strip().split(',')
        if line[1] in chessBoard:
            chessBoard[line[1]][1] = line[0]
            chessBoard[line[1]][2] = line[2]

pieceType = ['Pawn','Knight','Bishop','Queen','King','Rook']
possibleMoves = []
numPiecesMoved = 0
len_moves = 0
# Loop through every square, and every like-colored piece, and every move that can
# be made by that piece to determine all possible moves for a player
for square in chessBoard:
    foo = chessBoard[square]
    if foo[1] is not None and foo[2] == color:
        piece = getPieceID(foo[0][0], foo[0][1], foo[1], foo[2], pieceType)
        # Pawn
        if foo[1] == pieceType[0]:
            x,y = piece.moveForwardOne()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                    if (y == 7 and color == 'white') or (y == 0 and
                                                         color == 'black'):
                        possibleMoves[-1] = possibleMoves[-1] + \
                                            ' and may be promoted'
                bar = piece.getPosition()
                if chessBoard[key][1] == None and (bar[1] == 1 and color ==
                                                   'white') or (bar[1] == 6 and
                                                                color == 'black'):
                    x1,y1 = piece.moveForwardTwo()
                    a1,b1 = cartesianToChessCoord(x1,y1)
                    key1 = keyGenerator(a1,b1)
                    if chessBoard[key1][1] == None:
                        possibleMoves = moveWriter(possibleMoves,foo[1],square,key1)
            x,y = piece.captureLeft()
            a,b = cartesianToChessCoord(x,y)
            key = keyGenerator(a,b)
            if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                              chessBoard[key][1],key)
                if (y == 7 and color == 'white') or (y == 0 and color == 'black'):
                    possibleMoves[-1] = possibleMoves[-1] + ' and may be promoted'
            x,y = piece.captureRight()
            a,b = cartesianToChessCoord(x,y)
            key = keyGenerator(a,b)
            if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                              chessBoard[key][1],key)
                if (y == 7 and color == 'white') or (y == 0 and color == 'black'):
                    possibleMoves[-1] = possibleMoves[-1] + ' and may be promoted'
            if len(possibleMoves) != len_moves:
                len_moves = len(possibleMoves)
                numPiecesMoved += 1
        # Knight
        elif foo[1] == pieceType[1]:
            x,y = piece.moveLeftUp()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.moveRightUp()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.moveLeftDown()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.moveRightDown()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.moveUpLeft()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.moveUpRight()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None or chessBoard[key][2] == opponent:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.moveDownLeft()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.moveDownRight()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            if len(possibleMoves) != len_moves:
                len_moves = len(possibleMoves)
                numPiecesMoved += 1
        # Bishop
        elif foo[1] == pieceType[2]:
            x0,y0 = piece.getPosition()
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.diagUpLeft()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.diagUpRight()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.diagDownLeft()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.diagDownRight()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            if len(possibleMoves) != len_moves:
                len_moves = len(possibleMoves)
                numPiecesMoved += 1
        # Queen
        elif foo[1] == pieceType[3]:
            x0,y0 = piece.getPosition()
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.moveUp()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.moveDown()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.moveLeft()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.moveRight()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.diagUpLeft()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.diagUpRight()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.diagDownLeft()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.diagDownRight()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            if len(possibleMoves) != len_moves:
                len_moves = len(possibleMoves)
                numPiecesMoved += 1
        # King
        elif foo[1] == pieceType[4]:
            x,y = piece.moveUp()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.moveDown()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.moveLeft()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.moveRight()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.diagUpLeft()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.diagUpRight()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.diagDownLeft()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            x,y = piece.diagDownRight()
            if (0 <= x < 8) and (0 <= y < 8):
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                elif chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
            if len(possibleMoves) != len_moves:
                len_moves = len(possibleMoves)
                numPiecesMoved += 1
        # Rook
        elif foo[1] == pieceType[5]:
            x0,y0 = piece.getPosition()
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.moveUp()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.moveDown()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.moveLeft()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            piece.setPosition(x0,y0)
            x,y = x0,y0
            while 0 <= x < 8 and 0 <= y < 8:
                x,y = piece.moveRight()
                a,b = cartesianToChessCoord(x,y)
                key = keyGenerator(a,b)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][1] == None:
                    possibleMoves = moveWriter(possibleMoves,foo[1],square,key)
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == opponent:
                    possibleMoves = captureWriter(possibleMoves,foo[1],square,
                                                  chessBoard[key][1],key)
                    break
                if (0 <= x < 8) and (0 <= y < 8) and chessBoard[key][2] == color:
                    break
            if len(possibleMoves) != len_moves:
                len_moves = len(possibleMoves)
                numPiecesMoved += 1

possibleMoves.sort()
for line in possibleMoves:
    print line

print '%s legal moves (%s unique piece(s)) for %s player' % (len(possibleMoves),numPiecesMoved,color)

