Battleship
===========
A script to test strategies for the game of battleship.


### High scores

Strategy | Avg. Shots | Avg. Duration
---------|------------|---------------
[Horizontal Sweep](./strategies/horizontal_sweep.py) | 89 | .004s
[Random](./strategies/random_shot.py) | 95 | .004s


### Description

Each strategy should be specified as a function that takes
in the game board and returns the coordinates for a shot.

The game board renders 0s as untargeted spaces. -s as misses,
and X for hits. Unlike the game, the strategy function will not 
get information about which boats have been sunk.

For the standard game, there are five boats:
- 1 boat of length 5
- 1 boat of length 4
- 2 boats of length 3
- 1 boat of length 2

If you report your high scores (avg. shots and time per 1k runs),
and send in the code for your strategy, I'll post the results here.

### License
Licensed under [GNU GPL v3.0](./license.txt)
