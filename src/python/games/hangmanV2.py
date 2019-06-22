#!/usr/local/bin/python3

"""Hangman"""

import logging
import random

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.DEBUG)

HANGMAN_PICS = [
    '''
        +----+-
        |
        |
        |
        |
       =====''',
    '''
        +----+-
        |   O
        |
        |
        |
       =====''',
    '''
        +----+-
        |   O
        |   |
        |
        |
       =====''',
    '''
        +----+-
        |   O
        |   |\\
        |
        |
       =====''',
    '''
        +----+-
        |   O
        |  /|\\
        |
        |
       =====''',
    '''
        +----+-
        |   O
        |  /|\\
        |  /
        |
       =====''',
    '''
        +----+-
        |   O
        |  /|\\
        |  / \\
        |
       =====''']

EASY_WORDS = 'rack rank fame fly twin firm note gas jest eat fuss gate dare home ant fox myth wear peak mind lily ' \
             'run fold fix plan fax warn just boy sun cold rice frog walk thaw dawn fine date tree want meal look ' \
             'draw mill tap due drop age slow peel'.split()

MEDIUM_WORDS = 'passion glove behave outline romantic positive sacred hammer tenant speed crackpot item ferry' \
               'steam radio context win chapter hill clean rung retreat extinct sofa theft wonder charm daughter' \
               'mislead route hero show public money primary button layer ecstasy regard monopoly duck pigeon bomb ' \
               'set descent oppose honest minimum ministry album'.split()

HARD_WORDS = 'Awkward Bagpipes Banjo Bungler Croquet Crypt Dwarves Fervid Fishhook Fjord Gazebo Gypsy Haiku ' \
             'Haphazard Hyphen Ivory Jazzy Jiffy Jinx Jukebox Kayak Kiosk Klutz Memento Mystify Numbskull ' \
             'Ostracize Oxygen Pajama Phlegm Pixel Polka Quad Quip Rhythmic Rogue Sphinx Squawk Swivel Toady ' \
             'Twelfth Unzip Waxy Wildebeest Yacht Zealous Zigzag Zippy Zombie'.split()


def get_word(difficulty):
    if difficulty == '1':
        logging.debug('Getting an easy word')
        word_list = EASY_WORDS
    elif difficulty == '2':
        logging.debug('Getting a medium word')
        word_list = MEDIUM_WORDS
    elif difficulty == '3':
        logging.debug('Getting a hard word')
        word_list = HARD_WORDS

    word = random.choice(word_list).lower()
    logging.debug('Returning word ' + word)
    return word


def display_board(incorrect_letters, correct_letters, secret_word):
    print('\n* * * * * * * * * *\n    Hangman    \n* * * * * * * * * *\n')
    print(HANGMAN_PICS[len(incorrect_letters)])
    print()

    print('Incorrect Letters: ')
    for letter in incorrect_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
    print('Secret Word: ')
    for letter in blanks:
        print(letter, end=' ')
    print()


def play_game():
    logging.debug('Start of program')

    while True:
        print('\n* * * * * * * * * *\n    Hangman    \n* * * * * * * * * *\n')
        print('\n1. Easy\n2. Medium\n3. Hard')

        difficulty = str(input()).lower()

        if difficulty == 'qq':
            logging.debug('Quitting')
            print('Quitting game')
            break
        elif difficulty == '1' or '2' or '3':
            logging.debug('Difficulty is a valid choice')
            word = get_word(difficulty)
            correct_letters = ''
            incorrect_letters = ''
        else:
            print('That was not a valid choice')
            continue

        win_flag = False

        while not win_flag:
            display_board(incorrect_letters, correct_letters, word)

            guess = input('Guess a letter: ').lower()
            if guess == 'qq':
                win_flag = True
                break
            elif len(guess) != 1:
                print('Please enter a single letter.')
                continue
            elif guess in incorrect_letters + correct_letters:
                print('You have already guessed that letter. Choose again.')
                continue
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a LETTER')
                continue

            if guess in word:
                correct_letters = correct_letters + guess

                found_all_letters = True
                for i in range(len(word)):
                    if word[i] not in correct_letters:
                        found_all_letters = False
                        break

                if found_all_letters:
                    print('Yes the secret word is "{}"! You have won after {} guessed'.format(word,
                                                                                              len(incorrect_letters +
                                                                                                  correct_letters)))
                    win_flag = True
            else:
                incorrect_letters = incorrect_letters + guess

            if len(incorrect_letters) == len(HANGMAN_PICS) - 1:
                display_board(incorrect_letters, correct_letters, word)
                print('You have run out of guesses!\nAfter {} missed guesses and {} correct guesses,'
                      ' the word was {}'.format(str(len(incorrect_letters)), str(len(correct_letters)), word))
                win_flag = True


if __name__ == "__main__":
    play_game()
