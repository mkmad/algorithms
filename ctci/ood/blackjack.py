import random


class BlackJack(object):

    def __init__(self):
        self.deck = {
            'values': ['A', '2', '3', '4', '5', '6', '7',
                       '8', '9', '10', 'J', 'K', 'Q'],
            'type': ['Diamonds', 'Clubs', 'Spades', 'Hearts']
        }

        self.cards_drawn = []
        self.joker_count = 0

    def draw_card(self):
        if len(self.cards_drawn) <= 50:
            type_ = random.choice(self.deck['type'])
            value_ = random.choice(self.deck['values'])
            if type_ + '_' + value_ not in self.cards_drawn:
                self.cards_drawn.append(type_ + '_' + value_)
                return type_ + '_' + value_
            else:
                return self.draw_card()
        else:
            return None

    def hitme(self, dealer=False):
        current_value = 0
        values = []
        while current_value < 21:

            card = self.draw_card().split('_')
            if not dealer:
                print 'Player draws:', ''.join(card)
            else:
                print 'Dealer draws:', ''.join(card)
            values.append(card[1])
            if card[1] in ('J', 'K', 'Q'):
                current_value += 10
            elif card[1] == 'A':
                if current_value + 11 <= 21:
                    current_value += 11
                else:
                    current_value += 1
            else:
                current_value += int(card[1])

            if 17 <= current_value < 21:
                if not dealer:
                    # Choice of whether to stand or hit again
                    go_ahead = random.choice([True, False])
                    if go_ahead:
                        print 'Player has:', current_value
                        print 'Player decides to move forward'
                        continue
                    else:
                        print 'Player has:', current_value
                        print 'Player decides to stand'
                        break
                else:
                    print 'Dealer stands'
                    break

            if current_value > 21:
                if not dealer:
                    A_count = values.count('A')
                    while A_count:
                        current_value -= 10
                        if current_value < 21:
                            break
                        A_count -= 1

        if current_value <= 21:
            if current_value == 21:
                print 'Black Jack!!'
            return current_value
        else:
            return None

    def deal(self):
        print '\nPlayers Turn:'
        player = self.hitme(dealer=False)
        print '\nDealers Turn:'
        dealer = self.hitme(dealer=True)
        print
        if not player and dealer:
            print 'Player went over 21'
            print 'Dealer Wins with:', dealer

        if not dealer and player:
            print 'Dealer went over 21'
            print 'Player wins with:', player

        if player and dealer:
            print 'Player has:', player
            print 'Dealer has', dealer
            if player > dealer:
                print 'Player wins'
            elif dealer > player:
                print 'Dealer wins'
            else:
                print 'Both share the wins'

        if not player and not dealer:
            print 'Both player and Dealer went over 21'
            print 'No one wins'


if __name__ == '__main__':
    bj = BlackJack()
    bj.deal()
