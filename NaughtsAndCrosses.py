#!/usr/local/bin/python3

"""This is a tic tac toe game created by Jamie Coupe"""

import time

WIN_SLEEP_TIMER = 5


def print_board(board):
    print('\n* * * * * * * * * *\n Naughts and Crosses\n* * * * * * * * * *\n*                 *')
    print('*    ' + board['tl'] + ' | ' + board['tm'] + ' | ' + board['tr'] + '    *')
    print('*   ' + '---+---+---   *')
    print('*    ' + board['ml'] + ' | ' + board['mm'] + ' | ' + board['mr'] + '    *')
    print('*   ' + '---+---+---   *')
    print('*    ' + board['ll'] + ' | ' + board['lm'] + ' | ' + board['lr'] + '    *')
    print('*                 *\n* * * * * * * * * *\n')


def add_turn_to_board(board, move, turn):
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


def check_horizontal(board):
    for horizontal in range(3):
        row = [v for v in list(board.values())[horizontal * 3:(horizontal + 1) * 3]]
        # print('horizontal' + str(i) + str(row))
        if check_player_win(row):
            return player_wins()
        elif check_computer_win(row):
            return computer_wins()


def check_vertical(board):
    for vertical in range(3):
        row = [v for v in list(board.values())[vertical::3]]
        # print('vertical' + str(i) + str(row))
        if check_player_win(row):
            return player_wins()
        elif check_computer_win(row):
            return computer_wins()


def check_diagonal(board):
    for diagonal in range(0, 2):
        row = [v for v in list(board.values())[diagonal * 2::get_diagonal_multiplier(diagonal)]]
        if len(row) > 3:
            row.pop(3)
        # print('diagonal' + str(row))
        if check_player_win(row):
            return player_wins()
        elif check_computer_win(row):
            return computer_wins()


def get_diagonal_multiplier(i):
    if i == 1:
        return 2
    else:
        return 4


def check_win(board):
    horizontal = check_horizontal(board)
    vertical = check_vertical(board)
    diagonal = check_diagonal(board)

    if horizontal or vertical or diagonal:
        return True


def computer_wins():
    global board
    board = get_new_board()
    print('Computer wins')
    time.sleep(WIN_SLEEP_TIMER)
    return True


def player_wins():
    global board
    board = get_new_board()
    print('Player wins')
    time.sleep(WIN_SLEEP_TIMER)
    return True


def get_new_board():
    newboard = {'tl': ' ', 'tm': ' ', 'tr': ' ',
                'ml': ' ', 'mm': ' ', 'mr': ' ',
                'll': ' ', 'lm': ' ', 'lr': ' '}
    return newboard


def play_game():
    while True:

        board = get_new_board()
        turn = set_turn_from_choice()

        print_board(board)

        for i in range(9):
            if i > 0:
                print_board(board)

            won = check_win(board)

            if won:
                break
                print('No one win. Please try again!')

            move = input('Turn for ' + turn + '. Move on which space?').lower()

            if move == 'q':
                quitflag = True
                print('Quiting the game')
                break
            elif move in ['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'll', 'lm', 'lr']:
                if add_turn_to_board(board, move, turn):
                    turn = change_turn(turn)
                else:
                    continue
            else:
                print('Please enter a valid move')


if __name__ == "__main__":
    play_game()