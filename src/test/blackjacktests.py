import unittest
from src.python.games import blackjack

class blackjackTest(unittest.TestCase):

  def test_deal_hands_produces_two_hand_deck(self):
    self.assertEqual(2,blackjack.deal_hands())
