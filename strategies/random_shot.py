from random import randint

def random_shot(board):
    while True:
        x = randint(0,len(board)-1)
        y = randint(0,len(board)-1)
        if board[x][y] not in ["X","-"]:
            return x,y