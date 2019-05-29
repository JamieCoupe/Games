'''Tests for the hangman game'''

import unittest
from src.python.games.hangman import *


class hangmanTest(unittest.TestCase):

    man = ''
    test_word = ''

    def setUp(self):
        global man
        global test_word
        man = {'head' : '', 'left_arm': '', 'body': '', 'right_arm': '', 'left_leg': '', 'right_leg': ''}
        test_word = blank_word('can')

    def test_hang_man_can_block_out_a_word(self):
        self.assertEqual({'original': 'can', 'blanked': '---', 'counter': 0, 'letters': ''}, blank_word('can'))

    def test_correct_guess_will_un_blank_word(self):
        self.assertEqual('-a-', guess_letter(test_word, 'a')['blanked'])

    def test_can_get_easy_word(self):
        self.assertIn(get_word('1'), ['can', 'tan', 'apple'])

    def test_can_get_medium_word(self):
        self.assertIn(get_word('2'), ['medium', 'special', 'caravan'])

    def test_can_get_difficult_word(self):
        self.assertIn(get_word('3'), ['whisper', 'worship', 'arcane'])

    def test_get_man_for_each_counter(self):
        self.assertEqual({'head': 'O', 'left_arm': '', 'body': '', 'right_arm': '', 'left_leg': '', 'right_leg': ''},
                         get_man(1))

if __name__ == '__main__':
    unittest.main()
