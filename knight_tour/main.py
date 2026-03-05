from typing import List, Dict

def make_board(width:int , height: int ) -> Dict:
    touched = 0
    return {(i, j): touched for i in range(width) for j in range(height)}


print(make_board(5,5))


class knight:
    def __init__(self):
        pass
    def move(self, board:List, x:int, y:int):
        if (x,y) in board.keys():
            if not board[(x,y)]:
                board[(x, y)] = 1
        else:
            print('Moved out of the board!')
        return board

board= make_board(5,5)
k = knight()
print(k.move(board, 0, 2))
print(k.move(board, 1, 3))
