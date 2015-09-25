

# Generate a board with n number of randomly assigned piece types and colors


from random import randint as rnd


def keyGenerator(a,b):
    key = '%s' % a +':'+ '%s' % b
    return key


# Define piece types, locations on the board, and colors
pieceType = ['Pawn','Knight','Bishop','Queen','King','Rook']
chessBoard = {}
columns = ['A','B','C','D','E','F','G','H']
rows = [1,2,3,4,5,6,7,8]
for i in columns:
    for j in rows:
        key = keyGenerator(i,j)
        chessBoard[key] = ''
keys = []
for key in chessBoard:
    keys.append(key)

# Create the board and write to a file, where the headers are:
# Piece Type,Coordinates,Color
n = int(raw_input('How many pieces do you want? '))
colors = ['white','black']
n_keys = []
with open('randomBoard.txt','w') as data:
    for i in range(n):
        foo = rnd(0,len(keys))
        n_keys.append(keys[foo])
        keys.pop(foo)
        data.write('%s,%s,%s\n' % (pieceType[rnd(0,5)],n_keys[i],colors[rnd(0,1)]))