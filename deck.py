"""Module for a 52-card deck."""

import random
from card import Card

class Deck:
    """Deck class represents a standard 52-card deck."""
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        """TODO comment here."""
        random.shuffle(self.cards)

    def deal(self):
        """TODO comment here."""
        return self.cards.pop()
