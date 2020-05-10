class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.chips = 10

    def greeting(self):
        print("Hello, I am {}, nice to meet you".format(self.name))

    def get_card(self, cards):
        self.cards += cards

    def showhand(self):
        print("{} Card : {}".format(self.name, [card.show() for card in self.cards]))

    def bet(self, amount):
        if self.chips <= amount:
            print('There are not enough amount for the beg')
        self.chips -= amount
