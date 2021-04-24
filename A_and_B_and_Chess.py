"""
A and B are preparing themselves for programming contests.

To train their logical thinking and solve problems better, A and B decided to play chess. During the game A wondered whose position is now stronger.

For each chess piece we know its weight:

the queen's weight is 9,
the rook's weight is 5,
the bishop's weight is 3,
the knight's weight is 3,
the pawn's weight is 1,
the king's weight isn't considered in evaluating position.
The player's weight equals to the sum of weights of all his pieces on the board.

As A doesn't like counting, he asked you to help him determine which player has the larger position weight.

"""

board = [input() for i in range(8)]
all_pieces = []

for row in board :
    for coin in row  :
        all_pieces.append(coin)

Black_weight = {'q' :9, 'r':5, 'b':3, 'n':3, 'p':1}
White_weight = {'Q' :9, 'R':5, 'B':3, 'N':3, 'P':1}

def totalWeight(color, all_pieces) :
    weight = 0
    for i in color.keys() :
        weight += (all_pieces.count(i) * color[i])
    return weight

Black, White = totalWeight(Black_weight, all_pieces) , totalWeight(White_weight, all_pieces)

if Black > White :
    print("Black")
elif Black < White :
    print("White")
else:
    print("Draw")
