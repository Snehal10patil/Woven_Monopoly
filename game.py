from typing import List, Dict, Optional
from player import Player
from board import Board

class Game:
    def __init__(self, board: Board, players: List[Player], dice_rolls: List[int]):
        self.board = board
        self.players = players
        self.dice_rolls = dice_rolls
        self.current_player_index = 0

    def play(self):
        for roll in self.dice_rolls:
            current_player = self.players[self.current_player_index]
            if current_player.is_bankrupt():
                self._next_player()
                continue

            new_position = (current_player.position + roll) % self.board.size
            current_player.position = new_position
            self._handle_space(current_player, new_position)

            if new_position < current_player.position:
                current_player.add_money(1)

            self._next_player()

    def _handle_space(self, player: Player, position: int):
        space = self.board.get_space(position)
        if space["type"] == "property":
            owner = self._find_property_owner(space["name"])
            if owner is None:
                if player.money >= space["price"]:
                    player.deduct_money(space["price"])
                    player.add_property(space["name"])
            elif owner != player:
                rent = self._calculate_rent(space, owner)
                player.deduct_money(rent)
                owner.add_money(rent)

    def _find_property_owner(self, property_name: str) -> Optional[Player]:
        for player in self.players:
            if player.owns_property(property_name):
                return player
        return None

    def _calculate_rent(self, space: Dict, owner: Player) -> int:
        rent = space["price"]
        colour = space["colour"]
        monopoly = all(
            s["colour"] != colour or self._find_property_owner(s["name"]) == owner
            for s in self.board.spaces
            if s["type"] == "property"
        )
        return rent * 2 if monopoly else rent

    def _next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def get_results(self) -> Dict:
        results = {
            "players": [],
            "winner": None,
        }
        max_money = -1

        for player in self.players:
            space = self.board.get_space(player.position)
            results["players"].append({
                "name": player.name,
                "money": player.money,
                "position": space["name"],
            })
            if player.money > max_money and not player.is_bankrupt():
                max_money = player.money
                results["winner"] = player.name

        return results