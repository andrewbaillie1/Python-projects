# class game

from tkinter.tix import Tree
from cards import Card
import random


# grid size
# card options
# locations
# methods
# create cards
# create grid
# check for matches
# check game won
# run game


# create game instance
# call start game

class Game:
    def __init__(self):
        self.size = 4
        self.card_options = ['Add', 'Boo', 'Cat',
                             'Dev', 'Egg', 'Far', 'Gum', 'Hut']
        self.columns = ['A', 'B', 'C', 'D']
        self.locations = []
        self.cards = []
        for column in self.columns:
            for num in range(1, self.size + 1):
                location = f'{column}{num}'
                self.locations.append(f'{column}{num}')

    def set_cards(self):
        used_locations = []
        for word in self.card_options:
            for i in range(2):
                available_locations = set(self.locations) - set(used_locations)
                random_location = random.choice(list(available_locations))
                used_locations.append(random_location)
                card = Card(word, random_location)
                self.cards.append(card)

    def create_row(self, num):
        row = []
        for column in self.columns:
            for card in self.cards:
                if card.location == f'{column}{num}':
                    if card.matched:
                        row.append(str(card))
                    else:
                        row.append('   ')
        return row

    def create_grid(self):
        # /  A  /  B  /  C  /  D  /
        header = ' |  ' + '  |  '.join(self.columns) + '  |'
        print(header)
        for row in range(1, self.size + 1):
            print_row = f'{row}| '
            get_row = self.create_row(row)
            print_row += ' | '.join(get_row) + ' |'
            print(print_row)

    def check_match(self, loc1, loc2):
        cards = []
        for card in self.cards:
            if card.location == loc1 or card.location == loc2:
                cards.append(card)
        if cards[0] == cards[1]:
            cards[0].matched = True
            cards[1].matched = True
            return True
        else:
            for card in cards:
                print(f'{card.location}: {card}')
            return False

    def check_win(self):
        for card in self.cards:
            if card.matched == False:
                return False
        return True

    def check_location(self, time):
        while True:
            guess = input(f"What is the location of your {time} card? ")
            if guess.upper() in self.locations:
                return guess.upper()
            else:
                print(f"That guess wasn't valid")

    def start_game(self):
        game_running = True
        print("Memory Game")
        self.set_cards()
        while game_running:
            self.create_grid()
            guess1 = self.check_location('first')
            guess2 = self.check_location('second')
            if self.check_match(guess1, guess2):
                if self.check_win():
                    print('Congratulations, you won!')
                    self.create_grid()
                    game_running = False
            else:
                input('Those cards were not a match')
        print('Game over')


# dunder main
if __name__ == '__main__':
    game = Game()
    game.start_game()
    game.set_cards()
    game.create_grid()
