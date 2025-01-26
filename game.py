"""TODO comment here."""

from dealer import Dealer

class Game:
    """TODO comment here."""
    def __init__(self):
        self.players = []
        self.dealer = Dealer()
        self.pot = 0

    def add_player(self, player):
        """TODO comment here."""
        self.players.append(player)

    def start_game(self):
        """TODO comment here."""
        self.dealer.reset_game()
        for player in self.players:
            for _ in range(2):
                self.dealer.deal_to_player(player)

    def betting_round(self):
        """TODO comment here."""
        for player in self.players:
            bet = min(10, player.chips)  # Example: Minimum bet of 10 chips
            self.pot += player.bet(bet)

    def showdown(self):
        """TODO comment here."""
        # Simplified logic to determine a winner
        print("Showdown logic here")

    def reset(self):
        """TODO comment here."""
        self.pot = 0
        for player in self.players:
            player.hand = []
