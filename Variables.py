import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        self.suit = random.choice(suits)
        self.rank = random.choice(ranks)
        selected_card = f'{self.rank} of {self.suit}'
        return selected_card


class Deck:

    def __init__(self):
        self.deck = []
        self.shuffled_deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(f'{rank} of {suit}')

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        pass

    def __str__(self):
        Deck.shuffle(self)
        return str(self.deck)


print(Card(suits, ranks))
print(Deck())
