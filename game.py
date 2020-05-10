from player import Player
from Card import Card, Deck
from rule import Compare


class Game:
    def __init__(self):
        pass

    def start(self):
        player_1_name = input("What is your name (Player 1): ")
        player_1 = Player(player_1_name)
        player_2_name = input("What is your name (Player 2): ")
        player_2 = Player(player_2_name)

        # Start a new round of a game
        while player_1.chips >= 1 or player_2.chips >= 1:
            round = Round()
            loser, amount = round.start(player_1, player_2)
            print(f"{loser} lost this game for number of chips {amount}")
            if loser == player_1.name:
                player_2.chips += amount
            elif loser == player_2.name:
                player_1.chips += amount
            self.game_summary([player_1, player_2])
            player_1.cards = []
            player_2.cards = []
            print("\n\n")

        print('Game Over')

    def game_summary(self, player_list):
        print(f"-----------------------------------")
        print("This is a summary of this game")
        for player in player_list:
            print("{} has {} remaining chips".format(player.name, player.chips))
            print("Cards for {} : ".format(player.name))
            player.showhand()
        print(f"-----------------------------------")


class Round:
    def __init__(self):
        self.chips_on_table = 0

    def accept_bet(self, amount):
        self.chips_on_table += amount

    def start(self, player_1, player_2):
        # Create a new deck
        deck = Deck()
        deck.shuffle()

        # Random Greeting
        player_1.greeting()
        player_2.greeting()

        # Distribute the card
        player_1.get_card(deck.give_card(2))
        player_2.get_card(deck.give_card(2))

        # Distribute the card
        player_1.bet(1)
        player_2.bet(1)
        self.chips_on_table += 2

        # Play in two people way
        for term in range(3):
            for player in [player_1, player_2]:
                print(f"-----------------------------------")
                print(f"This is Player {player.name} term")
                print('This is the cards in players hand')
                player_1.showhand()
                player_2.showhand()
                print(f"-----------------------------------")
                action = int(input('Do you want to bet (1) or quit (0): '))
                if action == 1:
                    amount = int(input('Input the betting amount: '))
                    player.bet(amount)
                    player.get_card(deck.give_card(1))
                    self.chips_on_table += amount
                elif action == 0:
                    return player.name, self.chips_on_table

                print("\n")

        checker = Compare()
        if checker.compare(player_1.cards, player_2.cards):
            return player_2.name, self.chips_on_table
        else:
            return player_1.name, self.chips_on_table


if __name__ == "__main__":
    game_1 = Game()
    game_1.start()

