"""Function printing python version."""

class Player:
    """Function printing python version."""
    def __init__(self, name, chips=1000):
        self.name = name
        self.hand = []
        self.chips = chips

    def add_card(self, card):
        """TODO comment here."""
        self.hand.append(card)

    def show_hand(self):
        """TODO comment here."""
        return ', '.join(str(card) for card in self.hand)

    def bet(self, amount):
        """TODO comment here."""
        self.chips -= amount
        return amount
