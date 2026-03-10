# Knight's Tour

A small Python project that simulates the Knight’s Tour problem on a chess board.

The program creates a board, moves a knight across it, and logs the path taken until no more moves are available.

The board is then printed with the step number showing the order in which squares were visited.

## Run
```
python3 main.py board_width board_height play_method
```

play_method:
```
- default: always choosing first available cell to move
- random: choosing randomly among available cells
- warnsdorff: choosing cell based on Warnsdorff's rule
- warnsdorff_random: choosing cell based on Warnsdorff's rule but randomly among cells with same score
```