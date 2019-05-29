#!/usr/local/bin/python3
"""A program to launch the games"""

import os
import time
import NaughtsAndCrosses
import Hangman

while True:
    print('Available games:\n'
          '1. Naughts and Crosses\n'
          '2. Hangman')

    game = input('Which game would you like to play?').lower()

    if game == 'q':
        print('Quitting')
        break
    elif game == '1':
        os.system('clear')
        NaughtsAndCrosses.play_game()
    elif game == '2':
        os.system('clear')
        Hangman.play_game()
    else:
        print('Please enter a valid game number')

time.sleep(3)
os.system('clear')
exit()
