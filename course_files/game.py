import random


class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, value):
        if suit not in Card.suits and value not in Card.values:
            # raise ValueError(f"Card {value} of {suit} isn't exist!")
            raise ValueError("Card {} of {} isn't exist!".format(value, suit))
        self.suit = suit
        self.value = value

    def __repr__(self):
        # return f"{self.value} of {self.suit}"
        return "{} of {}".format(self.value, self.suit)


class Deck:

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        # return f"Deck of {self.count()} cards"
        return "Deck of {} cards".format(self.count())

    def __iter__(self):
        # for card in self.cards:   # using generators
        #     yield card
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        count = self.count()
        actual = min([count, number])
        if count == 0:
            raise ValueError("All cards have been dealt")
        deal_cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return deal_cards

    def shuffle(self):
        if self.count() == 52:
            random.shuffle(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, number):
        return self._deal(number)


deck = Deck()
print(deck.count())
print(deck)
deck.shuffle()

for card in deck:
    print(card)

card = deck.deal_card()
print(card)
hand = deck.deal_hand(100)
print(hand)
print(deck)

