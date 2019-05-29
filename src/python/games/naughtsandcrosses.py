#!/usr/local/bin/python3

"""This is a tic tac toe game created by Jamie Coupe"""

import time

WIN_SLEEP_TIMER = 5
COMPUTER_WIN = ['O', 'O', 'O']
PLAYER_WIN = ['X', 'X', 'X'] 

def print_board(board_dict):
    print('\n* * * * * * * * * *\n Naughts and Crosses\n* * * * * * * * * *\n*                 *')
    print('*    {} | {} | {}    *'.format(board_dict['tl'],board_dict['tm'],board_dict['tr']))
    print('*   ---+---+---   *')
    print('*    {} | {} | {}    *'.format(board_dict['ml'],board_dict['mm'],board_dict['mr']))
    print('*   ---+---+---   *')
    print('*    {} | {} | {}    *'.format(board_dict['ll'], board_dict['lm'], board_dict['lr'])) 
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
    is_valid_choice = True
    while is_valid_choice:
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
    if row == COMPUTER_WIN:
        return True
    else:
        return False


def check_player_win(row):
    if row == PLAYER_WIN:
        return True
    else:
        return False


def check_horizontal(board):
    for horizontal_index in range(3):
        horizontal_row = [v for v in list(board.values())[horizontal_index * 3:(horizontal_index + 1) * 3]]
        # print('horizontal' + str(i) + str(row))
        if check_player_win(horizontal_row):
            return player_wins()
        elif check_computer_win(horizontal_row):
            return computer_wins()


def check_vertical(board):
    for vertical_index in range(3):
        vertical_row = [v for v in list(board.values())[vertical_index::3]]
        # print('vertical' + str(i) + str(row))
        if check_player_win(vertical_row):
            return player_wins()
        elif check_computer_win(vertical_row):
            return computer_wins()


def check_diagonal(board):
    for diagonal_index in range(0, 2):
        diagonal_row = [v for v in list(board.values())[diagonal_index * 2::get_diagonal_multiplier(diagonal_index)]]
        if len(diagonal_row) > 3:
            diagonal_row.pop(3)
        # print('diagonal' + str(row))
        if check_player_win(diagonal_row):
            return player_wins()
        elif check_computer_win(diagonal_row):
            return computer_wins()


def get_diagonal_multiplier(i):
    if i == 1:
        return 2
    else:
        return 4


def check_win(board):
    horizontal_win = check_horizontal(board)
    vertical_win = check_vertical(board)
    diagonal_win = check_diagonal(board)

    if horizontal_win or vertical_win or diagonal_win:
        return True


def computer_wins():
    print('Computer wins')
    time.sleep(WIN_SLEEP_TIMER)
    return True


def player_wins():
    print('Player wins')
    time.sleep(WIN_SLEEP_TIMER)
    return True


def reset_board():
    board = {'tl': ' ', 'tm': ' ', 'tr': ' ',
                 'ml': ' ', 'mm': ' ', 'mr': ' ',
                 'll': ' ', 'lm': ' ', 'lr': ' '}
    return board


def play_game():
    while True:

        board = reset_board()
        turn = set_turn_from_choice()

        print_board(board)

        for i in range(9):
            if i > 0:
                print_board(board)


            if not check_win(board) and i == 9:
                print('No one won!')
                break

            move = input('Turn for ' + turn + '. Move on which space?').lower()

            if move == 'q':
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