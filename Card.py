import itertools
import random
from rule import Compare
from player import Player


class Card:
    def __init__(self, number, pattern):
        self.number = number
        self.pattern = pattern

    def show(self):
        return self.number, self.pattern


class Deck:
    def __init__(self):
        CARD_NUM = [x for x in range(1,14)]
        CARD_PATTERN = ['Diamond', 'Club', 'Hearts', 'Spade']
        self.deck = [Card(num, pattern) for num, pattern in itertools.product(CARD_NUM, CARD_PATTERN)]
        self.num = len(self.deck)

    def show_deck(self):
        return self.deck

    def shuffle(self):
        random.shuffle(self.deck)

    def give_card(self, num):
        cards = self.deck[:num]
        self.deck = self.deck[num:]
        return cards


# Create Player
def test():
    alex = Player("Alex")
    edward = Player("Edward")

    # Create Deck and shuffle
    deck = Deck()
    deck.shuffle()

    # Give card to Player
    card_on_table_1 = deck.give_card(5)
    alex.get_card(card_on_table_1)
    card_on_table_2 = deck.give_card(5)
    edward.get_card(card_on_table_2)

    # Show hand
    alex.greeting()
    alex.showhand()
    edward.greeting()
    edward.showhand()
    game_1 = Compare()

    if game_1.compare(alex.cards, edward.cards):
        print("Alex wins this game")
    else:
        print("edward wins this game")


if __name__ == "__main__":
    test()
