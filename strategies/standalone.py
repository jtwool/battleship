#! /usr/bin/python3

def horizontal_sweep(board):
    for x,row in enumerate(board):
        for y,space in enumerate(row):
            if space not in ["X", "-"]:
                return x, y

if __name__ == "__main__":
    import json, sys
    board = json.loads(sys.argv[1])
    shot_location = horizontal_sweep(board)
    print(json.dumps(shot_location))