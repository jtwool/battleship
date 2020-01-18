from random import randint

def random_shot(board):
    while True:
        x = randint(0,9)
        y = randint(0,9)
        if board[x][y] not in ["X","-"]:
            return x,y