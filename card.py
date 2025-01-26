"""Module for Card OOP class"""

class Card:
    """Card class represents a standard card in Texas Hold'em."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def get_rank(self):
        """Getter function for the card's rank."""
        return self.rank
    
    def get_suit(self):
        """Getter function for the card's suit."""
        return self.suit
