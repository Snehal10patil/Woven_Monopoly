import json
from board import Board
from player import Player
from game import Game

def load_json(file_path: str) -> list:
    """Load JSON data from a file."""
    with open(file_path, "r") as file:
        return json.load(file)

def main():
    # Load board and dice rolls
    board_data = load_json("board.json")
    dice_rolls1 = load_json("rolls_1.json")
    dice_rolls2 = load_json("rolls_2.json")

    # Combine rolls1 and rolls2 into a single list
    combined_dice_rolls = dice_rolls1 + dice_rolls2

    # Initialize board and players
    board = Board(board_data)
    players = [Player("Peter"), Player("Billy"), Player("Charlotte"), Player("Sweedal")]

    # Simulate game with combined dice rolls
    game = Game(board, players, combined_dice_rolls)
    game.play()

    # Get and print results
    results = game.get_results()
    print("Results for combined rolls:")
    for player in results["players"]:
        print(f"{player['name']} ends with ${player['money']} on {player['position']}")
    print(f"The winner is {results['winner']}")

if __name__ == "__main__":
    main()