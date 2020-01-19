"""A script to test strategies for the game of battleship.

An naive strategy -- random_shot() -- is provided.

Each strategy should be specified as a function that takes
in the game board and returns the coordinates for a shot.

The game board renders 0s as untargeted spaces. -s as misses,
and X for hits. Unlike the game, the strategy function will not 
get information about which boats have been sunk.

For the standard game, there are five boats:
1 boat of length 5
1 boat of lenght 4
2 boats of length 3
and 1 boat of length 2

Licensed under GNU GPL v3.0
"""
import time, logging, random

def new_board(n=10, boats=[5,4,3,3,2], empty=False):
    """Creates an n x n battleship board."""
    empty_board = [[0 for _ in range(n)] for _ in range(n)]
    if empty: return empty_board
    return place_boats(boats, empty_board)


def spot_is_empty(xs):
    """Check if a spot is empty"""
    return all(map(lambda x:x==0, xs))

def spot_is_long_enough(xs, boat):
    """Check if a spot is long enough to fit a boat"""
    return len(xs)==boat

def find_horizontal_valid_spots(boat, board):
    """Find valid horizontal spots for a boat of size boat"""
    valid_spots = []
    for i,row in enumerate(board):
        for j,x in enumerate(row):
           spot = row[j:j+boat]
           if (spot_is_empty(spot) and spot_is_long_enough(spot, boat)):
               valid_spots.append([(i,x) for x in range(j,j+boat)])
    return valid_spots

def find_vertical_valid_spots(boat, board):
    """Find valid vertical spots for a boat of size boat"""
    valid_spots = []
    for i,row in enumerate(board):
        if i+boat <= len(board):
            for j,_ in enumerate(row):
                spot = [board[x][j] for x in range(i,i+boat)]
                if (spot_is_empty(spot) and spot_is_long_enough(spot, boat)):
                    valid_spots.append([(x,j) for x in range(i,i+boat)])
    return valid_spots

def place_boat(boat, board, fn):
    """Place the boat in a spot determined by fn"""
    spots = fn(boat, board)
    spot = random.choice(spots)
    for x,y in spot:
        board[x][y] = boat
    logging.info("{}-boat placed.".format(boat))
    return board

def place_boats(boats, board):
    """Place boats on a battleship board."""
    for boat in boats:
        orientation = random.randint(0,1)
        if orientation == 0:
            board = place_boat(boat, board, find_horizontal_valid_spots)
        else:
            board = place_boat(boat, board, find_vertical_valid_spots)
    return board

def shot_did_hit(x,y,board):
    return board[x][y] not in [0,"X"]

def take_a_shot(shoot_function, game_state):
    """Resovle a shot."""
    x,y = shoot_function(game_state["tracking_board"])
    if shot_did_hit(x,y,game_state["board"]):
        game_state["tracking_board"][x][y] = "X"
        game_state["board"][x][y] = "H"
        logging.info("Shot at {},{} hit.".format(x,y))
    else:
        game_state["tracking_board"][x][y] = "-"
        game_state["board"][x][y] = "M"
        logging.info("Shot at {},{} missed.".format(x,y))
    game_state['shots'] += 1
    return game_state

def game_not_over(game_state, boats):
    """Check if any boats remain on the game board."""
    for row in game_state["board"]:
        for spot in row:
            if spot in [2,3,4,5]:
                return True
    return False

def summarize_games(game_results):
    """Summarize the results of many battleship games."""
    
    def min_avg_max(xs):
        return min(xs), sum(xs)/len(xs), max(xs), 

    all_shots = [g['shots'] for g in game_results]
    all_times = [g['duration'] for g in game_results]

    print("Shots: {:>3}, {:>3.0f}, {:>3}".format(*min_avg_max(all_shots)))
    print("Times: {:>3.3f}, {:>3.3f}, {:>3.3f}".format(*min_avg_max(all_times)))

def play_battleship(shoot_function, boats=[5,4,3,3,2], size=10, rounds=1):
    """Play the game of battleship."""
    def play():
        logging.info("New game.")
        game_state = {
            "board": new_board(size, boats=boats),
            "tracking_board": new_board(size, empty=True),
            "shots": 0,
            "start_time": time.time(),
        }
        while game_not_over(game_state, boats):
            game_state = take_a_shot(shoot_function, game_state)
        game_state['end_time'] = time.time()
        game_state['duration'] = game_state['end_time'] - game_state['start_time']
        return game_state

    results = [play() for _ in range(rounds)]
    return results

def pprint_battleship(game):
    """Pretty printing for a single game of battleship."""
    print("Shots: {:>3}, Duration {:>3.3f}s".format(game['shots'], game['duration']))
    for row in game['tracking_board']:
        print("".join(map(str, row)))

if __name__ == "__main__":
    logging.basicConfig(filename="battleship.log", level=logging.INFO)
    from strategies.random_shot import random_shot
    from strategies.horizontal_sweep import horizontal_sweep
    
    print("Random Shot")
    summarize_games(play_battleship(random_shot, rounds=1000))
    print("Horizontal Sweep")
    summarize_games(play_battleship(horizontal_sweep, rounds=1000))