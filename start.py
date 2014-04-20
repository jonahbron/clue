#!/usr/bin/python3.4

from game import Game
import sys

if len(sys.argv) >= 2 and sys.argv[1] == '--reset':
    reset_gamefile = True
else:
    reset_gamefile = False

if __name__ == "__main__":
    game = Game()
    game.play(reset_gamefile)
