
'''A game of blackjack'''

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.DEBUG)

while True:
    logging.debug('Blackjack has started')

    print('\n* * * * * * * * * *\n    Blackjack    \n* * * * * * * * * *\n')
    action = input('Make an action: T twist, S stick').lower()
    logging.debug('Action choosen was {}'.format(action))

    if action == 'qq':
        break
    elif action == 't':
        draw_hand(hand)
        print(calculate_score)
