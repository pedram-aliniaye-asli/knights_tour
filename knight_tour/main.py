from typing import List, Dict

def make_board(width:int , height: int ) -> Dict:
    touched = 0
    return {(i, j): touched for i in range(width) for j in range(height)}


# print(make_board(5,5))


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
# k = knight()
# print(k.move(board, 0, 2))
# print(k.move(board, 1, 3))


def cell_touched(board:List, x:int, y:int):
    return board[(x, y)]

def available_moves(board:List, x:int, y:int):
    av_moves = []
    max_y = max(k[1] for k in board.keys())
    max_x = max(k[0] for k in board.keys())
    min_y = min(k[1] for k in board.keys())
    min_x = min(k[0] for k in board.keys())
    print(max_y,max_x,min_y,min_x)
    #check right side
    if (y + 2) <= max_y:
        print('1')
        #check down side
        if (x + 1) <= max_x:
            if not cell_touched(board,x+1, y+2):
                av_moves.append((x+1, y+2))
        #check up side
        if (x - 1) >= min_x:
            if not cell_touched(board,x-1, y+2):
                av_moves.append((x-1,y+2))
    #check left side
    if (y - 2) >= min_y:
        print('2')

        #check down side
        if (x + 1) <= max_x:
            if not cell_touched(board,x+1, y-2):
                av_moves.append((x+1, y-2))
        #check up side
        if (x - 1) >= min_x:
            if not cell_touched(board,x-1, y-2):
                av_moves.append((x-1,y-2))
    #check down side
    if (x + 2) <= max_x:
        print('3')

        #check right side
        if (y + 1) <= max_y:
            if not cell_touched(board,x+2, y+1):
                av_moves.append((x+2, y+1))
        #check left side
        if (y - 1) >= min_y:
            if not cell_touched(board,x+2, y-1):
                av_moves.append((x+2, y-1))
    #check up side
    if (x - 2) >= min_x:
        print('4')

        #check right side
        if (y + 1) <= max_y:
            if not cell_touched(board,x-2, y+1):
                av_moves.append((x-2, y+1))
        #check left side
        if (y - 1) >= min_y:
            if not cell_touched(board,x-2, y-1):
                av_moves.append((x-2, y-1))
    return av_moves



board = make_board(3,3)
print(board)
a = available_moves(board,0,0)
print(a)
a = available_moves(board,1,0)
print(a)
a = available_moves(board,2,2)
print(a)
