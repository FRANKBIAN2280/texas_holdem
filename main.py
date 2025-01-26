"""Driver Modole for Python."""

from game import Game
from player import Player

def main():
    """Function printing python version."""
    game = Game()
    game.add_player(Player("Alice"))
    game.add_player(Player("Bob"))
    game.start_game()

    print("Starting hands:")
    for player in game.players:
        print(f"{player.name}: {player.show_hand()}")

    game.betting_round()
    print(f"Pot: {game.pot}")

    game.showdown()

if __name__ == "__main__":
    main()
