import Elements.player_queue
import Elements.dice
from Elements.player import Player
from builders.cellCiruitBuilder import CircuitBuilder

class Board:


    __board = None

    def __init__(self):
        self.first_cell, self.last_cell = CircuitBuilder.build()
        self.dice = Elements.dice.Dice()
        self.player_queue = Elements.player_queue.PlayerQueue()

    def __str__(self):
        return  "Board | "

    def __new__(cls, *args, **kwargs):
        if cls.__board is None:
            cls.__board = Board()
        return cls.__board

    def insert_player_to_the_first_cell(self, player):
        player.occupying_cell = self.first_cell
        player.reduce_remaining_moves()
        self.first_cell.move_in_player(player)