"""Module for a Texas hold'em dealer."""

from deck import Deck

class Dealer:
    """TODO comment here."""
    def __init__(self):
        self.deck = Deck()
        self.community_cards = []

    def deal_to_player(self, player):
        """TODO comment here."""
        player.add_card(self.deck.deal())

    def deal_community_cards(self, n):
        """TODO comment here."""
        for _ in range(n):
            self.community_cards.append(self.deck.deal())

    def reset_game(self):
        """TODO comment here."""
        self.deck = Deck()
        self.deck.shuffle()
        self.community_cards = []
