# HumbleBundleCodingChallenge

This is a script that takes in a file containing 3 columns:
-Piece type (pawn, knight, etc)
-Coordinates (location on the chess board like A:3, C:7)
-Color (white or black)

and, given which player's turn it is, returns all possible moves that every piece of that color can make, along with the number of pieces that can move. Also included is a script, randomBoard.py, that asks for an integer and randomly distributes randomly generated pieces, which is then written
to a file randomBoard.txt. This can be tested in the chessMoves.py script.

The file initialConditions.txt contains your standard chessboard setup which produces the output, for the white player:

Knight at <B:1> can move to <A:3>
Knight at <B:1> can move to <C:3>
Knight at <G:1> can move to <F:3>
Knight at <G:1> can move to <H:3>
Pawn at <A:2> can move to <A:3>
Pawn at <A:2> can move to <A:4>
Pawn at <B:2> can move to <B:3>
Pawn at <B:2> can move to <B:4>
Pawn at <C:2> can move to <C:3>
Pawn at <C:2> can move to <C:4>
Pawn at <D:2> can move to <D:3>
Pawn at <D:2> can move to <D:4>
Pawn at <E:2> can move to <E:3>
Pawn at <E:2> can move to <E:4>
Pawn at <F:2> can move to <F:3>
Pawn at <F:2> can move to <F:4>
Pawn at <G:2> can move to <G:3>
Pawn at <G:2> can move to <G:4>
Pawn at <H:2> can move to <H:3>
Pawn at <H:2> can move to <H:4>
20 legal moves (10 unique piece(s)) for white player

