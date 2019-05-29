#!/usr/local/bin/python3

"""Hangman"""

import logging
import random
import time

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.DEBUG)

EASY_WORDS = ['can', 'tan', 'apple']
MEDIUM_WORDS = ['medium', 'special', 'caravan']
HARD_WORDS = ['whisper', 'worship', 'arcane']


def blank_word(word_to_blank):
    blanked_word = ''

    for letter in enumerate(word_to_blank):
        blanked_word += '-'

    all_words = {'original': word_to_blank, 'blanked': blanked_word, 'counter': 0, 'letters': ''}
    return all_words


def blank_word_guess(all_words, guess):
    logging.debug('Guess is ' + guess)
    original_word = str(all_words['original'])
    guessed_word = str(all_words['blanked'])
    new_guessed = ''
    counter = all_words['counter']
    for letter_index in range(len(original_word)):
        logging.debug('Letter index is ' + str(letter_index))
        if original_word[letter_index] in guessed_word or original_word[letter_index] == guess:
            logging.debug('Letter is the guess or already guessed')
            new_guessed += original_word[letter_index]
        else:
            logging.debug('Letter is not a match to this letter moving onto the next')
            new_guessed += '-'

    all_words = {'original': original_word, 'blanked': new_guessed, 'counter': counter, 'letters': all_words['letters']}
    return all_words


def guess_letter(words, guess):
    original_word = str(words['original'])
    if guess in original_word:
        print('Guess %s was correct' % guess)
        words = blank_word_guess(words, guess)
    elif guess in words['letters']:
        print('You have guessed this letter before')
    else:
        print('Guess %s was incorrect' % guess)
        words['counter'] = words['counter'] + 1
        words['letters'] = words['letters'] + ' ' + guess
    logging.debug('The returned words are ' + str(words))
    return words


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


def get_word_list(filename):
    with open(filename) as word_file:
      return [word.rstrip('\n') for word in word_file]


def get_easy_word():
    logging.debug('Getting an easy word')
    words = get_word_list('easy.txt')
    word = random.choice(words)
    logging.debug('Returning word ' + word)
    return word


def get_medium_word():
    logging.debug('Getting an medium word')
    words = get_word_list('medium.txt')
    word = random.choice(words)
    logging.debug('Returning word ' + word)
    return word


def get_hard_word():
    logging.debug('Getting an hard word')
    words = get_word_list('hard.txt')
    word = random.choice(words)
    logging.debug('Returning word ' + word)
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


def check_if_lost(words):
    if len(words['letters']) >= 12:
        man = get_man(words['counter'])
        print_gallows(man)
        print('\n* * * * * * * * * *\n You lost! \n* * * * * * * * * *\n')
        time.sleep(5)
        return False
    else:
        return True


def check_if_won(words):
    if '-' not in words['blanked']:
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
            words = blank_word(word)
        else:
            print('That was not a valid choice')

        win_flag = True

        while win_flag:

            print('\n* * * * * * * * * *\n    Hangman    \n* * * * * * * * * *\n' +
                  words['blanked'] + '\n' + 'Guesses:' + words['letters'])
            man = get_man(words['counter'])
            print_gallows(man)
            guess = input('Make a guess: ')
            if len(guess) == 1:
                words = guess_letter(words, guess)
            else:
                print('Only guess one letter at a time')

            win_flag = check_if_won(words)
            win_flag = check_if_lost(words)


if __name__ == "__main__":
    play_game()
