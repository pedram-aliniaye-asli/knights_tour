from typing import List, Dict, Tuple
import random

Board = Dict[Tuple[int, int], int]
Position = Tuple[int, int]


def make_board(width: int, height: int) -> Board:
    touched = 0
    return {(x, y): touched for x in range(width) for y in range(height)}


class Knight:
    def __init__(self):
        pass

    def move(self, board: Board, x: int, y: int) -> Board:
        if (x, y) in board:
            if not board[(x, y)]:
                board[(x, y)] = 1
        else:
            print("Moved out of the board!")
        return board

    def log_moves(self, moves: List[Position], x: int, y: int) -> List[Position]:
        moves.append((x, y))
        return moves


def get_board_limits(board: Board) -> Dict[str, int]:
    max_y = max(y for _, y in board.keys())
    max_x = max(x for x, _ in board.keys())
    min_y = min(y for _, y in board.keys())
    min_x = min(x for x, _ in board.keys())

    return {
        "max_y": max_y,
        "max_x": max_x,
        "min_y": min_y,
        "min_x": min_x,
    }


def is_cell_touched(board: Board, x: int, y: int) -> int:
    return board[(x, y)]


def available_moves(board: Board, x: int, y: int) -> List[Position]:
    moves = []
    limits = get_board_limits(board)

    max_y = limits["max_y"]
    max_x = limits["max_x"]
    min_y = limits["min_y"]
    min_x = limits["min_x"]

    # check right side
    if (y + 2) <= max_y:
        # check down side
        if (x + 1) <= max_x:
            if not is_cell_touched(board, x + 1, y + 2):
                moves.append((x + 1, y + 2))

        # check up side
        if (x - 1) >= min_x:
            if not is_cell_touched(board, x - 1, y + 2):
                moves.append((x - 1, y + 2))

    # check left side
    if (y - 2) >= min_y:
        # check down side
        if (x + 1) <= max_x:
            if not is_cell_touched(board, x + 1, y - 2):
                moves.append((x + 1, y - 2))

        # check up side
        if (x - 1) >= min_x:
            if not is_cell_touched(board, x - 1, y - 2):
                moves.append((x - 1, y - 2))

    # check down side
    if (x + 2) <= max_x:
        # check right side
        if (y + 1) <= max_y:
            if not is_cell_touched(board, x + 2, y + 1):
                moves.append((x + 2, y + 1))

        # check left side
        if (y - 1) >= min_y:
            if not is_cell_touched(board, x + 2, y - 1):
                moves.append((x + 2, y - 1))

    # check up side
    if (x - 2) >= min_x:
        # check right side
        if (y + 1) <= max_y:
            if not is_cell_touched(board, x - 2, y + 1):
                moves.append((x - 2, y + 1))

        # check left side
        if (y - 1) >= min_y:
            if not is_cell_touched(board, x - 2, y - 1):
                moves.append((x - 2, y - 1))

    return moves

def play(board: Board):
    moves: List[Position] = []
    knight = Knight()

    limits = get_board_limits(board)

    x = random.randint(limits["min_x"], limits["max_x"])
    y = random.randint(limits["min_y"], limits["max_y"])

    knight.move(board, x, y)
    knight.log_moves(moves, x, y)

    available = available_moves(board, x, y)

    while available:
        x, y = available[0]

        knight.move(board, x, y)
        knight.log_moves(moves, x, y)

        available = available_moves(board, x, y)

    return board, moves


def print_board(board: Board, moves: List[Position]) -> None:
    max_x = max(x for x, _ in board)
    max_y = max(y for _, y in board)

    step_map = {position: index + 1 for index, position in enumerate(moves)}

    for x in range(max_x + 1):
        row = []
        for y in range(max_y + 1):
            if (x, y) in step_map:
                row.append(f"{step_map[(x, y)]:2}")
            else:
                row.append(" .")
        print(" ".join(row))


board = make_board(5, 5)
final_board, moves = play(board)
print_board(final_board, moves)