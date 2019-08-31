

class Player:

    COUNT_NO_REMAINING_MOVES = 0

    def __init__(self, index, is_external_player=False):
        self.index = index
        self.is_external_player = is_external_player
        self.occupying_cell = None
        self.remaining_moves = self.COUNT_NO_REMAINING_MOVES

    def __str__(self):
        return f"Player Object | index:{self.index} |"

    def set_remaining_moves(self, remaining_moves):
        self.remaining_moves = remaining_moves

    def set_occupying_cell(self, cell):
        self.occupying_cell = cell


class CellCircuit:
    """
    The class should manage the circuit
    It provides interface to add a player to a certain cell, and manage where to move what
    """

    CELL_FIRST_CELL = 1

    def __init__(self):
        self.player_dict = {}

    def push_in_player_to_the_board(self, player):
        """
        function should be called when entry critera acheived for pushing the player
        add the player to the dictionary and set position as 1
        :param player: Player
        :return: None
        """
        self.player_dict[player] = self.CELL_FIRST_CELL

    def get_player_position(self, player):
        if player in self.player_dict.keys():
            return self.player_dict[player]
        else:
            raise Exception(f"player {player} not in the circuit")

    def get_board_status(self):
        pass
