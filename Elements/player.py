from Configurations import numbers
from Configurations import Strings
from Elements.board import Board

class Player:

    def __init__(self, id=0):
        self.index = id
        self.occupying_cell = None
        self.__remaining_movements = 0
        self.board = Board()

    def __str__(self):
        return "Player object | id:"+self.id+" | "

    def get_remaining_moves(self):
        return self.__remaining_movements

    def reduce_remaining_moves(self, count):
        self.__remaining_movements -= 1

    def set_remaining_moves(self, moves):
        self.__remaining_movements = moves
        if self.__remaining_movements == 1 and self.occupying_cell is None:
            Board.insert_player_to_the_first_cell()
        elif self.__remaining_movements > 0 and self.occupying_cell is not None:
            self.occupying_cell.move_out_player(self)