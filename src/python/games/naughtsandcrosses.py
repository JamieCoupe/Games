#!/usr/local/bin/python3

"""This is a tic tac toe game created by Jamie Coupe"""

import logging
import random
import time

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.DEBUG)

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


def set_turn_from_choice():
    is_valid_choice = True
    while is_valid_choice:
        choice = input('Who should play first?\n'
                       '1. You ("X")\n'
                       '2. Computer ("O")\n').lower()
        if choice == '1':
            return 'X'
        elif choice == '2':
            return 'O'
        elif choice == 'qq':
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
        logging.debug('horizontal' + str(horizontal_index) + str(horizontal_row))
        if check_player_win(horizontal_row):
            return player_wins()
        elif check_computer_win(horizontal_row):
            return computer_wins()


def check_vertical(board):
    for vertical_index in range(3):
        vertical_row = [v for v in list(board.values())[vertical_index::3]]
        logging.debug('vertical' + str(vertical_index) + str(vertical_row))
        if check_player_win(vertical_row):
            return player_wins()
        elif check_computer_win(vertical_row):
            return computer_wins()


def check_diagonal(board):
    for diagonal_index in range(0, 2):
        diagonal_row = [v for v in list(board.values())[diagonal_index * 2::get_diagonal_multiplier(diagonal_index)]]
        if len(diagonal_row) > 3:
            diagonal_row.pop(3)
            logging.debug('diagonal' + str(diagonal_row))
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


def add_turn_to_board(board, move, turn):
    if board[move] != ' ':
        print("This location has been used before\n Please try again.")
    else:
        board[move] = turn

    return board


def player_move(board, turn_number, turn):
    move = input('Turn for ' + turn + '. Move on which space?').lower()

    if move == 'qq':
        print('Quiting the game')
        return 'quit'
    elif move in ['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'll', 'lm', 'lr']:
        board = add_turn_to_board(board, move, turn)
    else:
        print('Please enter a valid move')

    return board


def computer_move2(board, turn_number, turn):
    free_spaces = []
    player_spaces = []
    computer_spaces = []
    for location, value in board.items():
        logging.debug('Location = ' + location)
        logging.debug('value = ' + value)
        if value == ' ':
            free_spaces.append(location)
            player_spaces.append('')
            computer_spaces.append('')
            logging.debug('Free spaces are ' + str(free_spaces))
        elif value == 'O':
            player_spaces.append(location)
            computer_spaces.append('')
            free_spaces.append('')
        elif value == 'X':
            computer_spaces.append(location)
            player_spaces.append('')
            free_spaces.append('')
        else:
            continue

    random.shuffle(free_spaces)
    location = free_spaces.pop()
    logging.debug('chosen location is ' + location)
    board = add_turn_to_board(board, location, turn)
    return board


def computer_move(board, turn):
    # Here is the algorithm for our Tic-Tac-Toe AI:
    # First, check if we can win in the next move.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    # Check if the player could win on their next move and block them.
    for i in range(1, 10):
        # Return True if every space on the board has been taken. Otherwise,
        return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
    boardCopy = getBoardCopy(board)
    if isSpaceFree(boardCopy, i):
        makeMove(boardCopy, playerLetter, i)
    if isWinner(boardCopy, playerLetter):
        return i
    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    return 5
    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def play_game():
    while True:

        board = reset_board()
        turn = set_turn_from_choice()

        print_board(board)

        for turn_number in range(9):
            if turn == 'X':
                board = player_move(board, turn_number, turn)

                if not check_win(board) and turn_number == 9:
                    print('No one won!')
                    break

                turn = change_turn(turn)
                print_board(board)

                if board == 'quit':
                    break
                time.sleep(2)
                board = computer_move(board, turn_number, turn)
                print_board(board)

                if not check_win(board) and turn_number == 9:
                    print('No one won!')
                    break

                turn = change_turn(turn)
            else:
                time.sleep(2)
                board = computer_move(board, turn_number, turn)

                if not check_win(board) and turn_number == 9:
                    print('No one won!')
                    break

                turn = change_turn(turn)
                print_board(board)

                if board == 'quit':
                    break

                board = player_move(board, turn_number, turn)
                print_board(board)

                if not check_win(board) and turn_number == 9:
                    print('No one won!')
                    break

                turn = change_turn(turn)


if __name__ == "__main__":
    play_game()