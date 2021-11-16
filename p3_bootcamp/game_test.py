import unittest
from p3_bootcamp.game import Card, Deck


class CardTests(unittest.TestCase):

    def setUp(self):
        self.card = Card("Hearts", "A")

    def test_init(self):
        """Cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        """repr should return a string of the form 'VALUE of SUIT'"""
        self.assertEqual(repr(self.card), "A of Hearts")


class DeckTests(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """Deck should have 52 cards"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """repr should return a string of the form 'Deck of {count} cards'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    # def test_iter(self):
    #     """Should return next card in deck"""
    #     print([iter(self.deck)])
    #     self.assertEqual([iter(self.deck)], [iter(self.deck.cards)])

    def test_count(self):
        """Full deck must have 52 cards"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_sufficient_cards(self):
        """_deal should deal the number of cards"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient_cards(self):
        """_deal should deal the number of cards left in the deck"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        """_deal should throw a ValueError if the deck is empty"""
        cards = self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_card_is_exist(self):
        """Card's suit and value must be permitted"""
        card = self.deck.deal_card()
        self.assertIn(card.suit, Card.suits)

    def test_deal_card(self):
        """deal_card should deal a single card from the deck"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        """deal_handDeck should deal the number of cards passed in params"""
        cards = self.deck.deal_hand(51)
        self.assertEqual(len(cards), 51)
        self.assertEqual(self.deck.count(), 1)

    def test_hand_after_deal(self):
        """Hand must have 10 cards after dealing 10 cards"""
        hand = self.deck.deal_hand(10)
        self.assertEqual(len(hand), 10)

    def test_shuffle_not_full_deck(self):
        """Only full decks can be shuffled"""
        self.deck.deal_card()
        with self.assertRaises(ValueError):
            self.deck.shuffle()

    def test_shuffle_full_deck(self):
        """The order of cards before and after shuffle must be different"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)


if __name__ == "__main__":
    unittest.main()
