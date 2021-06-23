import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values =  {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:
    def __init__(self, s, r):
        self.suit = s.capitalize()
        self.rank = r.capitalize()
        self.value = values[r]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


player_one = Player("Possum")
player_two = Player("Beescuit")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


game_on = True

round_num = 0

while game_on:

    round_num += 1
    print(f'\nRound{round_num}')

    if len(player_one.all_cards) == 0:
        print(f'{player_one.name}, Out of cards! {player_two.name} Wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(f'{player_two.name}, Out of cards! {player_one.name} Wins!')
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        time.sleep(0.5)

        if player_one_cards[-1].value > player_two_cards[-1].value:
            print(f"{player_one.name}'s {player_one_cards[-1]} defeated {player_two_cards[-1]}")

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False


        elif player_one_cards[-1].value < player_two_cards[-1].value:
            print(f"{player_two.name}'s {player_two_cards[-1]} defeated {player_one_cards[-1]}")

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False


        else:
            print('\nWAR!\ndraw 5 cards')

            if len(player_one.all_cards) < 7:
                print(f'{player_one.name} unable to declare war')
                print(f"{player_two.name} wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < 7:
                print(f'{player_two.name} unable to declare war')
                print(f"{player_one.name} wins!")
                game_on = False
                break

            else:
                for num in range(7):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())





