"""Four in a row"""

import logging
import random

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.DEBUG)


def get_board():
    logging.debug('Getting board')

    board = [[' '] * 7 for row in range(6)]
    return board


def get_turn():
    while True:
        choice = input('Who will play first?\n1. User\n2. Computer')
        if choice == '1':
            return 'X'
        elif choice == '2':
            return 'O'
        elif choice.lower() == 'qq':
            return 'quit'
        else:
            print('Please enter 1 or 2')


def print_board(board):
    logging.debug('Printing board, row by row')
    print('| 0 |  1 |  2 |  3 |  4 |  5 |  6 |')
    for row in board:
        print(row)
    print('\n')
    return


def get_free_row(column, board):
    logging.debug('Getting free rows')
    column_list = []
    for row in board:
        logging.debug('Row is {}'.format(row))
        column_list.append(row[column])
    logging.debug('Column is {}'.format(column_list))
    logging.debug('Getting lowest free row')

    row_index = -1

    for space in column_list:
        if space == ' ':
            row_index += 1
        else:
            break

    logging.debug('The lowest free row is'.format(row_index))
    return row_index


def make_move(column_index, board, turn):
    row_index = get_free_row(column_index, board)
    logging.debug('Making move at col = {}, row = {} for turn {}'.format(column_index, row_index, turn))
    board[row_index][column_index] = turn
    logging.debug('New board after move is {}'.format(board))
    return board


def change_turn(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'


def player_turn(board):
    logging.debug('Player is taking their turn')

    column = input('Enter the column you want to play: ')
    if column == 'qq':
        logging.debug('Quitting current run of game')
        return 'break'

    elif column == '' or int(column) > 6:
        logging.debug('The user did not enter a valid value: {}'.format(column))
        print('\nEnter a valid number 0-7 or "qq" to quit')
        return 'continue'

    column = int(column)
    turn = 'O'
    board = make_move(column, board, 'O')

    return board


def computer_turn(board):
    turn = 'X'
    column = random.randint(0, 7)
    board = make_move(column, board, 'X')

    return board


def play_game():
    logging.debug('Starting Four in a Row')

    while True:

        board = get_board()
        won = False
        turn = get_turn()

        if turn == 'quit':
            logging.debug('Quitting game now')
            break

        while not won:
            print('\n* * * * * * * * * *\n   Four in a Row\n* * * * * * * * * *\n')
            print_board(board)

            old_board = board
            board = player_turn(board)

            if board == 'continue':
                board = old_board
                continue
            elif board == 'break':
                won = True
                break

            turn = change_turn(turn)

            board = computer_turn(board)


if __name__ == "__main__":
    play_game()
