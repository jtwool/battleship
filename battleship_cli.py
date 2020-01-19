"""CLI for running battleship strategies from any programming language.

Uses JSON as data interchange format.

For scripts to be compatible, they should be

1. Executables
2. Take a JSON array in -- the board representation
3. Output a two element JSON array -- the coordinates of the shot

Python example included in strategies/standalone.py
"""
import subprocess, argparse, json, logging
from subprocess import PIPE
from battleship import summarize_games, play_battleship

if __name__ == "__main__":    
    logging.basicConfig(filename="battleship.log", level=logging.INFO)
    
    parser = argparse.ArgumentParser(description="A battleship strategy evaluator.")
    parser.add_argument("-f", "--file", required=True,
                        help="Path to battleship strategy script.")
    parser.add_argument("-n", "--runs", default=1, type=int,
                        help="Number of runs to perform. 1000 is standard for evaluation.")
    

    args = parser.parse_args()

    def shoot_function_external(board):
        """Take a shot with an external script"""
        json_board = json.dumps(board)
        shot = subprocess.run([args.file, json_board], 
                               stdout=PIPE, encoding="ascii")
        x,y = json.loads(shot.stdout)
        return x,y

    summarize_games(play_battleship(shoot_function_external, rounds=args.runs))