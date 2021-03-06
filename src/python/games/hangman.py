#!/usr/local/bin/python3

"""Hangman"""

import logging
import random
import time

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.DEBUG)


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
    new_guessed = ''
    counter = game_variables['counter']
    for letter_index in range(len(original_word)):
        logging.debug('Letter index is ' + str(letter_index))
        if original_word[letter_index] in guessed_word or original_word[letter_index] == guess:
            logging.debug('Letter is the guess or already guessed')
            new_guessed += original_word[letter_index]
        else:
            logging.debug('Letter is not a match to this letter moving onto the next')
            new_guessed += '-'

    game_variables = {'original': original_word, 'blanked': new_guessed, 'counter': counter,
                      'letters': game_variables['letters']}
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

    logging.debug('The returned words are ' + str(game_variables))
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

    print(gallows['first_row']+'\n'+gallows['second_row']+'\n'+gallows['third_row']+'\n'+gallows['fourth_row']+'\n' +
          gallows['fifth_row']+'\n'+gallows['sixth_row']+'\n'+gallows['seventh_row']+'\n'+gallows['eighth_row']+'\n' +
          gallows['ninth_row'])


def get_word(difficulty):
    if difficulty == '1':
        return get_easy_word()
    elif difficulty == '2':
        return get_medium_word()
    elif difficulty == '3':
        return get_hard_word()

# /Users/jamiecoupe/PycharmProjects/Games/src/data/easywords.txt


def get_word_list(filename):
    with open('/Users/jamiecoupe/PycharmProjects/Games/src/data/{}'.format(filename)) as word_file:
        return [word.rstrip('\n') for word in word_file]


def get_easy_word():
    logging.debug('Getting an easy word')
    words = get_word_list('easywords.txt')
    word = random.choice(words)
    logging.debug('Returning word ' + word)
    return word


def get_medium_word():
    logging.debug('Getting an medium word')
    words = get_word_list('mediumwords.txt')
    word = random.choice(words)
    logging.debug('Returning word ' + word)
    return word


def get_hard_word():
    logging.debug('Getting an hard word')
    words = get_word_list('hardwords.txt')
    word = random.choice(words)
    logging.debug('Returning word ' + word)
    return word


def get_man(turn_counter, man):
    logging.debug('Getting the man')

    if turn_counter == 1:
        man['head'] = '    O'
    elif turn_counter == 2:
        man['body_top'] = '    |'
        man['body_bottom'] = '    |'
    elif turn_counter == 3:
        man['body_top'] = '|'
        man['left_arm'] = '   \\'
    elif turn_counter == 4:
        man['right_arm'] = '/'
    elif turn_counter == 5:
        man['left_leg'] = '    /'
    elif turn_counter == 6:
        man['right_leg'] = '\\'
    logging.debug('Man is:' + str(man))
    return man


def check_if_lost(game_variables, man):
    if len(game_variables['letters']) >= 12:
        man = get_man(game_variables['counter'], man)
        print_gallows(man)
        print('\n* * * * * * * * * *\n You lost! \n The word was: {}\n* * * * * * * * * *\n'.format(
            game_variables['original'].capitalize()))
        time.sleep(5)
        return True
    else:
        return False


def check_if_won(game_variables):
    if '-' not in game_variables['blanked']:
        logging.debug('Player one')
        print('\n* * * * * * * * * *\n You win, congratulations! \n* * * * * * * * * *\n')
        time.sleep(3)
        return True
    else:
        return False


def play_game():
    logging.debug('Start of program')

    while True:
        print('\n* * * * * * * * * *\n    Hangman    \n* * * * * * * * * *\n')
        print('\n1. Easy\n2. Medium\n3. Hard')

        difficulty = str(input()).lower()
        man = {'head': '', 'left_arm': '', 'body_top': '', 'right_arm': '', 'body_bottom': '', 'left_leg': '',
               'right_leg': ''}

        if difficulty == 'qq':
            logging.debug('Quitting')
            print('Quitting game')
            break
        elif difficulty == '1' or '2' or '3':
            logging.debug('Difficulty is a valid choice')
            word = get_word(difficulty)
            game_variables = blank_word(word)
        else:
            print('That was not a valid choice')

        win_flag = False

        while not win_flag:

            print('\n* * * * * * * * * *\n    Hangman    \n* * * * * * * * * *\n\nWord: {}\nGuesses: {}\n'.format(
                game_variables['blanked'], game_variables['letters']))

            man = get_man(game_variables['counter'], man)
            print_gallows(man)
            guess = input('Make a guess: ')

            if guess == 'qq':
                logging.debug("Quitting game")
                break
            if len(guess) == 1:
                game_variables = guess_letter(game_variables, guess)
            else:
                print('Only guess one letter at a time')

            win_flag = check_if_lost(game_variables, man) or check_if_won(game_variables)


if __name__ == "__main__":
    play_game()
