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
and send in the code for your strategy, I'll post the results here. (PRs appreciated.)

## Designing a `shoot_function`
Shoot functions should take the game board in and return two integers:
the coordinates of the desired shot. The first integer represents the 
row targeted and the second integer represents the cell targeted.

A 3x3 game board may look like this:

```python3
[[0, 0, 'X'],
 [0,'-', 0],
 [0, 0,  0]]
```

On this board, the cells 1,1 and 0,2 have been shot at.
Cell 1,1 was a miss -- represented by a `'-'` and cell 0,2 was a hit
represented by an `'X'`.

The shoot function would take this board and return another pair of coordinates,
for example: `(0,1)`.

Two example shoot functions are provided for reference: [random_shot.py](strategies/random_shot.py) and [horizontal_sweep.py](strategies/horizontal_sweep.py).

### Multi-language support

You can design shoot functions in any language you wish, using the [battleship_cli](./battleship_cli.py). This utility takes an executable script and uses that script as the shoot function. These shoot functions should expect a JSON array as input -- the board -- and print (only) a JSON array as output -- the location to shoot at next.

An example script is provided for reference: [standalone.py](strategies/standalone.py)

**NB**: Functions in languages other than Python will take longer to run because of system overhead.

## Designing shoot functions with AI

I've set up logging for the script to support training AI. If you'd like to use the system logs to
train AI, you can set the logging level to 24.

```python
if __name__ == "__main__":
    logging.basicConfig(filename="battleship.log", level=24)
```

You can also modify the output as you desire to produce logs in any format you please.

## License
Licensed under [GNU GPL v3.0](./license.txt)
