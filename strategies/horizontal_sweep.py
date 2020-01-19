def horizontal_sweep(board):
    for x,row in enumerate(board):
        for y,space in enumerate(row):
            if space not in ["X", "-"]:
                return x, y
