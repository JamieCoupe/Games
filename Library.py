#!/usr/local/bin/python3
"""A program to launch the games"""

import os
import time

while True:
    print('Available games:\n'
          '1. Naughts and Crosses')

    game = input('Which game would you like to play?').lower()

    if game == 'q':
        print('Quitting')
        break
    elif game == '1':
        os.system('python3 ~/PycharmProjects/Games/NaughtsAndCrosses.py')
    else:
        print('Please enter a valid game number')

time.sleep(3)
os.system('clear')
exit()
