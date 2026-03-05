from typing import List, Dict

def make_board(width:int , height: int ) -> Dict:
    touched = 0
    return {(i, j): touched for i in range(width) for j in range(height)}


print(make_board(5,5))
