
'''A game of blackjack'''

import logging
import random
import time 

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.DEBUG)

def generate_deck():
  hearts = [card for card in range(1,14)]
  diamonds = [card for card in range(1,14)]
  clubs = [card for card in range(1,14)]
  spades = [card for card in range(1,14)]
  deck = hearts + diamonds + clubs + spades
  random.shuffle(deck)
  return deck


def deal_hands(deck):
  hands = [[deck.pop(),deck.pop()],[deck.pop(),deck.pop()]] 
  return hands 


def translate_hand(hand):
  translated_hand = []
  for card in hand:
    if card == 1: 
      translated_hand.append('Ace')
    elif card == 11:
      translated_hand.append('Jack')
    elif card == 12:
      translated_hand.append('Queen')
    elif card == 13:
      translated_hand.append('King')
    else:
      translated_hand.append(card)
  
  return translated_hand


def calculate_total(hand):
  total = 0 
  for card in hand:
    total += card
  return total


def twist(deck,hand):
  hand.append(deck.pop())
  return hand


def check_loss(hand):
  if calculate_total(hand) > 21:
    return True
  else: 
    return False

def players_turn(deck,hand):
  while True:
    print('\n* * * * * * * * * *\n    Blackjack    \n* * * * * * * * * *\n')
    print("Your hand is: {}. Total: {}".format(translate_hand(hand),calculate_total(hand)))

    if check_loss(hand):
      break

    action = input('Make an action: T twist, S stick \n').lower()
    logging.debug('Action choosen was {}'.format(action))
    if action == 'qq':
      break
    elif action == 't':
      hand = twist(deck,hand)
    elif action == 's':
      return hand
    else:
      print("Please enter a valid option") 


def dealers_turn(deck,hand):
  while True: 
    total = calculate_total(hand)

    if check_loss(hand):
      break

    if total < 16: 
      print('Dealer is twisting')
      hand = twist(deck,hand)
      time.sleep(1)
    else: 
      print('Dealer has stuck')
      time.sleep(1)
      return hand
  return hand

  
def get_winner(player_hand,dealer_hand):
  player_total = calculate_total(player_hand)
  dealer_total = calculate_total(dealer_hand)

  if player_total > dealer_total: 
    print('Player wins with {}!'.format(player_total))
  elif player_total < dealer_total: 
    print('Dealer wins with {}!'.format(dealer_total))
  else:
    print('It was a draw!\nPlayer had: {}\nDealer had: {}'.format(player_total,dealer_total))


def play_game():
  while True:
      logging.debug('Blackjack has started')
      deck = generate_deck()
      hands = deal_hands(deck)
      player_hand = hands[0]
      dealer_hand = hands[1]
      
      player_hand = players_turn(deck,player_hand)
      if check_loss(player_hand):
        logging.debug('Player lost')
        print("You Lose you went higher than 21.\n")
        break

      dealer_hand = dealers_turn(deck,dealer_hand)
      if check_loss(dealer_hand):
        logging.debug('Dealer lost')
        print("Dealer has lost they higher than 21.\n")
        break

      get_winner(player_hand,dealer_hand)
      time.sleep(5)

        

if __name__ == "__main__":
    play_game()
