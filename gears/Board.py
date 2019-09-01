
import gears.elements
from gears.playerQueue import PlayerQueue


class Board:
    """
    board
    """
    current_player: gears.elements.Player

    def __init__(self, player_count: int = 2):
        self.count_player = player_count
        self.queue_player = PlayerQueue(player_count)
        for index in range(2):
            self.queue_player.create_player()
        self.circuit = gears.elements.CellCircuit()
        self.current_player = self.queue_player.get_next_player()
        self.dice = gears.elements.Dice()

    def get_board_state(self):
        return self.circuit.get_board_status()

    def get_player(self):
        return self.current_player

    def play(self):
        moves = self.dice.roll()
        self.current_player.set_remaining_moves(moves)
