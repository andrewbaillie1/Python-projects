class Card:
    def __init__(self, card, location):
        self.card = card
        self.location = location
        self.matched = False

    def __eq__(self, other):
        return self.card == other.card

    def __str__(self):
        return self.card


if __name__ == '__main__':
    card1 = Card('egg', 'A1')
    card2 = Card('egg', 'B1')
    card3 = Card('tea', 'B3')

    print(card1 == card2)
    print(card1 == card3)
    print(card1)
    print(card1.location)
