#!/usr/local/bin/python3

"""Hangman"""

import logging
import random
import time

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.DEBUG)

EASY_WORDS = ['can', 'tan', 'apple']
MEDIUM_WORDS = ['medium', 'special', 'caravan']
HARD_WORDS = ['Awkward', 'Bagpipes', 'BanjoBungler','Croquet','Crypt', 'Dwarves', 'Fervid', 'Fishhook', 'Fjord',
              'Gazebo', 'Gypsy', 'Haiku', 'Haphazard', 'Hyphen', 'Ivory', 'Jazzy', 'Jiffy', 'Jinx', 'Jukebox', 'Kayak',
              'Kiosk', 'Klutz', 'Memento', 'Mystify', 'Numbskull', 'Ostracize', 'Oxygen', 'Pajama', 'Phlegm', 'Pixel',
              'Polka', 'Quad', 'Quip', 'Rhythmic', 'Rogue', 'Sphinx', 'Squawk', 'Swivel', 'Toady', 'Twelfth', 'Unzip',
              'Waxy', 'Wildebeest', 'Yacht', 'Zealous','Zigzag', 'Zippy', 'Zombie']


def read_word_list(filename):
    with open(filename) as word_file:
      return word_file.readlines()
  
  
def blank_word(word_to_blank):
    blanked_word = ''

    for letter in enumerate(word_to_blank):
        blanked_word += '-'

    game_variables = {'original': word_to_blank, 'blanked': blanked_word, 'counter': 0, 'letters': ''}
    return game_variables


def blank_word_guess(game_variables, guess):
    logging.debug('Guess is ' + guess)
    original_word = str(game_variables['original'])
    guessed_word = str(game_variables['blanked'])
    new_guessed_word = ''
    counter = game_variables['counter']
    for letter_index in range(len(original_word)):
        logging.debug('Letter index is {}'.format(str(letter_index))
        if original_word[letter_index] in guessed_word or original_word[letter_index] == guess:
            logging.debug('Letter is the guess or already guessed')
            new_guessed_word  += original_word[letter_index]
        else:
            logging.debug('Letter is not a match to this letter moving onto the next')
            new_guessed_word  += '-'

    game_variables = {'original': original_word, 'blanked': new_guessed_word, 'counter': counter, 'letters': game_variables['letters']}
    return game_variables


def guess_letter(game_variables, guess):
    original_word = str(game_variables['original'])
    if guess in original_word:
        print('Guess %s was correct' % guess)
        game_variables = blank_word_guess(game_variables, guess)
    elif guess in game_variables['letters']:
        print('You have guessed this letter before')
    else:
        print('Guess %s was incorrect' % guess)
        game_variables['counter'] = game_variables['counter'] + 1
        game_variables['letters'] = game_variables['letters'] + ' ' + guess
    logging.debug('The returned words are {}'.format(str(game_variables)
    return game_variables


def print_gallows(man):
    gallows = {'first_row': '-------',
               'second_row': '|    |',
               'third_row': '|' + man['head'],
               'fourth_row': '|' + man['left_arm'] + man['body_top'] + man['right_arm'],
               'fifth_row': '|' + man['body_bottom'],
               'sixth_row': '|' + man['left_leg'] + man['right_leg'],
               'seventh_row': '| ',
               'eighth_row': '---------',
               'ninth_row': '|VVVVVVV|',
               }

    print(gallows['first_row']+'\n'+gallows['second_row']+'\n'+gallows['third_row']+'\n'+gallows['fourth_row']+'\n'+
          gallows['fifth_row']+'\n'+gallows['sixth_row']+'\n'+gallows['seventh_row']+'\n'+gallows['eighth_row']+'\n'+
          gallows['ninth_row'])


def get_word(difficulty):
    if difficulty == '1':
        return get_easy_word()
    elif difficulty == '2':
        return get_medium_word()
    elif difficulty == '3':
        return get_hard_word()


def get_easy_word():
    logging.debug('Getting an easy word')
    # words = read_word_list('easy.txt')
    words = EASY_WORDS
    word = str(random.choice(words)).lower
    logging.debug('Returning word {}'.format(word))
    return word


def get_medium_word():
    logging.debug('Getting an medium word')
    # words = read_word_list('medium.txt')
    words = MEDIUM_WORDS
    word = str(random.choice(words)).lower()
    logging.debug('Returning word {}'.format(word))
    return word


def get_hard_word():
    logging.debug('Getting an hard word')
    # words = read_word_list('hard.txt')
    words = HARD_WORDS
    word = str(random.choice(words)).lower()
    logging.debug('Returning word {}'.format(word))
    return word


def get_man(turn_counter):
    logging.debug('Getting the man')
    if turn_counter == 1:
        man = {'head': '    O', 'left_arm': '', 'body_top': '', 'right_arm': '', 'body_bottom': '', 'left_leg': '',
               'right_leg': ''}
    elif turn_counter == 2:
        man = {'head': '    O', 'left_arm': '', 'body_top': '    |', 'right_arm': '', 'body_bottom': '    |',
               'left_leg': '', 'right_leg': ''}
    elif turn_counter == 3:
        man = {'head': '    O', 'left_arm': '   \\', 'body_top': '|', 'right_arm': '', 'body_bottom': '    |',
               'left_leg': '', 'right_leg': ''}
    elif turn_counter == 4:
        man = {'head': '    O', 'left_arm': '   \\', 'body_top': '|', 'right_arm': '/', 'body_bottom': '    |',
               'left_leg': '', 'right_leg': ''}
    elif turn_counter == 5:
        man = {'head': '    O', 'left_arm': '   \\', 'body_top': '|', 'right_arm': '/', 'body_bottom': '    |',
               'left_leg': '     /', 'right_leg': ''}
    elif turn_counter == 6:
        man = {'head': '    O', 'left_arm': '   \\', 'body_top': '|', 'right_arm': '/', 'body_bottom': '    |',
               'left_leg': '    /', 'right_leg': '\\'}
    else:
        man = {'head' : '', 'left_arm': '', 'body_top': '', 'right_arm': '', 'body_bottom': '', 'left_leg': '',
               'right_leg': ''}
    logging.debug('Man is:' + str(man))
    return man


def check_if_lost(game_variables):
    if len(game_variables['letters']) >= 12:
        man = get_man(game_variables['counter'])
        print_gallows(man)
        print('\n* * * * * * * * * *\n You lost! \n* * * * * * * * * *\n')
        time.sleep(5)
        return False
    else:
        return True


def check_if_won(game_variables):
    if '-' not in game_variables['blanked']:
        logging.debug('No more letters to guess')
        print('\n* * * * * * * * * *\n You win, congratulations! \n* * * * * * * * * *\n')
        time.sleep(3)
        return False
    else:
        return True


def play_game():
    logging.debug('Start of program')

    while True:
        print('\n* * * * * * * * * *\n    Hangman    \n* * * * * * * * * *\n')
        print('\n1. Easy\n2. Medium\n3. Hard')

        difficulty = str(input()).lower()

        if difficulty == 'q':
            logging.debug('Quitting')
            print('Quitting game')
            exit()
        elif difficulty == '1' or '2' or '3':
            logging.debug('Difficulty is a valid choice')
            word = get_word(difficulty)
            game_variables = blank_word(word)
        else:
            print('That was not a valid choice')

        win_flag = True

        while win_flag:

            print('\n* * * * * * * * * *\n    Hangman    \n* * * * * * * * * *\n' +
                  game_variables['blanked'] + '\n' + 'Guesses:' + game_variables['letters'])
            man = get_man(game_variables['counter'])
            print_gallows(man)
            guess = input('Make a guess: ')
            if len(guess) == 1:
                game_variables = guess_letter(game_variables, guess)
            else:
                print('Only guess one letter at a time')

            win_flag = check_if_won(game_variables)
            win_flag = check_if_lost(game_variables)


if __name__ == "__main__":
    play_game()
