from typing import Dict
from random import randrange
import logging as log


class Player:

    COUNT_NO_REMAINING_MOVES = 0

    def __init__(self, index: int, name: str = None, is_external_player: bool = False):
        """
        creates a player object with name and index
        :param index: int
        :param name: str
        :param is_external_player: bool
        """
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
        """
        called for setting the count returned from the dice object
        :param remaining_moves: int
        :return: None
        """
        self.remaining_moves = remaining_moves
        log.debug(f"remaining moves set: {self.remaining_moves}")

    def set_occupying_cell(self, cell: int):
        """
        called to set the cell occupied by the player
        :param cell: Cell
        :return: None
        """
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

    COUNT_ENTRY_CRITERIA = 1

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
        if player.remaining_moves == CellCircuit.COUNT_ENTRY_CRITERIA:
            self.set_player_occupying_cell(player, CellCircuit.CELL_FIRST_CELL)
            log.debug(f"{player} pushed into the board")
        else:
            log.debug(f"{player} not to be pushed into the board")

    def get_player_position(self, player: Player):
        if player in self.player_dict.keys():
            return self.player_dict[player]
        else:
            raise Exception(f"player {player} not in the circuit")

    def move_player_on_the_board(self, player: Player):
        new_cell = self.player_dict[player] + player.remaining_moves
        if player.remaining_moves > Player.COUNT_NO_REMAINING_MOVES and new_cell <= CellCircuit.CELL_LAST_CELL:
            self.set_player_occupying_cell(player, new_cell)
            self.check_and_apply_special_movement(player)
            log.debug(f"{player} moved to {player.occupying_cell}")

    def check_and_apply_special_movement(self, player: Player):
        if self.player_dict[player] in self.CHAIN.keys():
            self.set_player_occupying_cell(player, self.CHAIN[self.player_dict[player]])
            log.info(f"{player} reached a special cell and moved to {player.occupying_cell}")
        CellCircuit.FLAG_VICTORY = self.check_if_victory_condition_achieved(player)

    def check_if_victory_condition_achieved(self, player: Player):
        if player.occupying_cell >= self.CELL_LAST_CELL:
            log.info(f"{player} victory condition ")
            return True
        return False

    def get_board_status(self):
        return self.player_dict

    def set_player_occupying_cell(self, player: Player, cell: int):
        self.player_dict[player] = cell
        player.set_occupying_cell(cell)


class Dice:
    """
    class dice is a single dice roller.
    used for generating s random numbers in the range of [1,6]
    """

    DICE_LOW = 1
    DICE_HIGH = 6

    @staticmethod
    def roll():
        roll_count = randrange(Dice.DICE_LOW, Dice.DICE_LOW+1)
        print(f"dice Rolled : {roll_count}")
        return roll_count
