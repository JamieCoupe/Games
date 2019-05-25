#!/usr/local/bin/python3

"""This is a tic tac toe game created by Jamie Coupe"""

import os
import time

WIN_SLEEP_TIMER = 5


def print_board(board):
    os.system('clear')
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
    print('-+-+-')
    print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
    print('-+-+-')
    print(board['ll'] + '|' + board['lm'] + '|' + board['lr'])


def add_turn_to_board():
    if board[move] != ' ':
        print("This location has been used before\n Please try again.")
        has_player = False
    else:
        board[move] = turn
        has_player = True

    return has_player


def set_turn_from_choice():
    validchoice = True
    while validchoice:
        choice = input('Who should play first?\n1. You ("X")\n2. Computer ("O")\n').lower()
        if choice == '1':
            return 'X'
        elif choice == '2':
            return 'O'
        elif choice == 'q':
            print('Quitting')
            exit()
        else:
            print('Please enter "1" or "2"')


def change_turn(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'


def check_computer_win(row):
    if row == ['O', 'O', 'O']:
        return True
    else:
        return False


def check_player_win(row):
    if row == ['X', 'X', 'X']:
        return True
    else:
        return False


def check_horizontal():
    for i in range(3):
        row = [v for v in list(board.values())[i * 3:(i + 1) * 3]]
        # print('horizontal' + str(i) + str(row))
        if check_player_win(row):
            player_wins()
        elif check_computer_win(row):
            computer_wins()


def check_vertical():
    for i in range(3):
        row = [v for v in list(board.values())[i::3]]
        # print('vertical' + str(i) + str(row))
        if check_player_win(row):
            player_wins()
        elif check_computer_win(row):
            computer_wins()


def check_diagonal():
    for i in range(0, 2):
        row = [v for v in list(board.values())[i * 2::get_diagonal_multiplier(i)]]
        if len(row) > 3:
            row.pop(3)
        # print('diagonal' + str(row))
        if check_player_win(row):
            player_wins()
        elif check_computer_win(row):
            computer_wins()


def get_diagonal_multiplier(i):
    if i == 1:
        return 2
    else:
        return 4


def check_win():
    check_horizontal()
    check_vertical()
    check_diagonal()


def computer_wins():
    global board
    board = get_new_board()
    print('Computer wins')
    time.sleep(WIN_SLEEP_TIMER)


def player_wins():
    global board
    board = get_new_board()
    print('Player wins')
    time.sleep(WIN_SLEEP_TIMER)


def get_new_board():
    newboard = {'tl': ' ', 'tm': ' ', 'tr': ' ',
                'ml': ' ', 'mm': ' ', 'mr': ' ',
                'll': ' ', 'lm': ' ', 'lr': ' '}
    return newboard


while True:

    board = get_new_board()

    turn = set_turn_from_choice()

    for i in range(9):
        print_board(board)
        check_win()

        move = input('Turn for ' + turn + '. Move on which space?').lower()

        if move == 'q':
            quitflag = True
            print('Quiting the game')
            break
        elif move in ['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'll', 'lm', 'lr']:
            if add_turn_to_board():
                turn = change_turn(turn)
            else:
                continue

        else:
            print('Please enter a valid move')

    print('No one win. Please try again!')
