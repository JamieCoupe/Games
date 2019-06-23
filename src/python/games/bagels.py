#!/usr/local/bin/python3

# This is the bagels deduction game created by
# jamie coupe based off the game found in
# Al Sweigarts' book"""

import random

NUM_DIGITS = 3
MAX_GUESS = 10


def get_secret_num():
    # Returns a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10))
    random.shuffle(numbers)

    secret_num = ''

    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    # Returns a string with the Pico, Fermi, & Bagels clues to the user.
    if guess == secret_num:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)


def is_only_digits(num):
    # Returns True if num is a string of only digits. Otherwise returns false.
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


def rules():
    print('I am thinking of a {} digit number. Try to guess whit it is'.format(NUM_DIGITS))
    print('The clues I give are...\n'
          'When I say: That means:\n'
          '     Bagels          None of digits is correct\n'
          '     Pico            One digit is correct but in the wrong position\n'
          '     Fermi           One digit is correct and in the right position\n'
          'Enter "r" as a guess to display the rules again\n')


def play_game():
    while True:
        rules()
        secret_num = get_secret_num()
        print('I have thought up a number. You have {} guesses to get it.\n'.format(MAX_GUESS))
        guesses_taken = 1

        progress = input('Enter anything to continue, enter "q" to quit')

        if progress.lower() == 'q':
            break

        while guesses_taken <= MAX_GUESS:

            print('Guess #{}: '.format(guesses_taken))
            guess = input()
            if guess == 'q':
                break
            elif guess == 'r':
                rules()
                continue

            while len(guess) != NUM_DIGITS or not is_only_digits(guess):
                print('Guess #{}: '.format(guesses_taken))
                guess = input()

            print(get_clues(guess, secret_num))
            guesses_taken += 1

            if guess == 'q':
                break
            elif guess == 'r':
                rules()
                continue
            elif guess == secret_num:
                break
            if guesses_taken > MAX_GUESS:
                print('You ran out of guesses. The answer was {}'.format(secret_num))

        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break


if __name__ == "__main__":
    play_game()
