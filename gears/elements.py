from typing import Dict
from random import randrange
import logging as log


class Player:

    COUNT_NO_REMAINING_MOVES = 0

    def __init__(self, index: int, name: str = None, is_external_player: bool = False):
        self.index = index
        if name is None:
            self.name = "Player"+str(index)
        else:
            self.name = name
        self.is_external_player = is_external_player
        self.occupying_cell = None
        self.remaining_moves = self.COUNT_NO_REMAINING_MOVES
        log.debug(f"player created: {self}")

    def __str__(self):
        return f"Player Object | index:{self.index} |"

    def set_remaining_moves(self, remaining_moves: int):
        self.remaining_moves = remaining_moves
        log.debug(f"remaining moves set: {self.remaining_moves}")

    def set_occupying_cell(self, cell: int):
        self.occupying_cell = cell
        log.debug(f"{self} is occupying cell: {self.occupying_cell}")


class CellCircuit:
    """
    The class should manage the circuit
    It provides interface to add a player to a certain cell, and manage where to move what
    """
    player_dict: Dict[Player, int]

    CELL_FIRST_CELL = 1
    CELL_LAST_CELL = 100

    FLAG_VICTORY = False

    CHAIN = {6: 27, 9: 50, 20: 39, 25: 57, 43: 16, 53: 72, 54: 58, 55: 34, 61: 82, 70: 48, 78: 42, 95: 73, 96: 82}

    def __init__(self):
        self.player_dict = {}

    def process_player(self, player: Player):
        if player.occupying_cell is None:
            self.push_in_player_to_the_board(player)
            log.debug(f"{player} remaining moves: {None}")
        else:
            self.move_player_on_the_board(player)
            log.debug(f"{player} remaining moves: {player.remaining_moves}")

    def push_in_player_to_the_board(self, player: Player):
        """
        function should be called when entry criteria achieved for pushing the player
        add the player to the dictionary and set position as 1
        :param player: Player
        :return: None
        """
        if player.remaining_moves == 1:
            self.player_dict[player] = self.CELL_FIRST_CELL
            player.set_occupying_cell(self.CELL_FIRST_CELL)
            log.debug(f"{player} pushed into the board")
        log.debug(f"{player} not to be pushed into the board")

    def get_player_position(self, player: Player):
        if player in self.player_dict.keys():
            return self.player_dict[player]
        else:
            raise Exception(f"player {player} not in the circuit")

    def move_player_on_the_board(self, player: Player):
        if player.remaining_moves > Player.COUNT_NO_REMAINING_MOVES and self.player_dict[player] + player.remaining_moves <= 100:
            self.player_dict[player] = self.player_dict[player] + player.remaining_moves
            player.occupying_cell = self.player_dict[player]
            self.check_and_apply_special_movement(player)
            log.debug(f"{player} moved to {player.occupying_cell}")

    def check_and_apply_special_movement(self, player: Player):
        if self.player_dict[player] in self.CHAIN.keys():
            self.player_dict[player] = self.CHAIN[self.player_dict[player]]
            player.occupying_cell = self.player_dict[player]
            log.info(f"{player} reached a special cell and moved to {player.occupying_cell}")
        if player.occupying_cell >= self.CELL_LAST_CELL:
            log.info(f"{player} victory condition ")
            CellCircuit.FLAG_VICTORY = True
            pass

    def get_board_status(self):
        return self.player_dict

    @staticmethod
    def get_victory_flag():
        return CellCircuit.FLAG_VICTORY


class Dice:
    """

    """

    @staticmethod
    def roll():
        roll_count = randrange(1, 7)
        print(f"dice Rolled : {roll_count}")
        return roll_count
