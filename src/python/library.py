#!/usr/local/bin/python3
"""A program to launch the games"""

import os
import time

from src.python.games import blackjack
from src.python.games import fourinarow
from src.python.games import hangman
from src.python.games import naughtsandcrosses


def main():
    while True:
        print('Available games:\n'
              '1. Naughts and Crosses\n'
              '2. Hangman\n'
              '3. Blackjack\n'
              '4. Four in a Row\n')

        game = input('Which game would you like to play?').lower()

        if game == 'q':
            print('Quitting')
            break
        elif game == '1':
            os.system('clear')
            naughtsandcrosses.play_game()
        elif game == '2':
            os.system('clear')
            hangman.play_game()
        elif game == '3':
            os.system('clear')
            blackjack.play_game()
        elif game == '4':
            os.system('clear')
            fourinarow.play_game()
        else:
            print('Please enter a valid game number')

    time.sleep(3)
    os.system('clear')
    exit()


if __name__ == "__main__":
    main()
