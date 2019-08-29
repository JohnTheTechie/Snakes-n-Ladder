from Elements.player import Player
import logging as log

class Cell:
    """
    Base class for cell
    """
    def __init__(self):
        self.index = None
        self.next_cell = None
        self.previous_cell = None
        self.connection_cell = None
        self.player_buffer = None
        self.kind = None
        self.occupant_player_list = []
        log.debug(f"{self} object created")


    def __str__(self):
        return f"Cell | index:{self.index} | "

    def move_out_player(self, player):
        if player in self.occupant_player_list:
            if player.get_remaining_moves() > 0:
                self.__move(player, self.next_cell, should_reduce_move=True)
            log.info(f"{self} has {player} in the list | player has {player.get_remaining_moves()} moves")
        else:
            log.info(f"{self} does not have {player} in the list")

    def move_in_player(self, player):
        self.player_buffer = player
        log.debug(f"{self}.")
        self.process_player_buffer()

    def process_player_buffer(self):
        if self.player_buffer.remaining_movement_count > 0:
            self.__move(self.player_buffer, self.next_cell, should_reduce_move=True)
            self.player_buffer = None
        elif self.connection_cell is None:
            self.occupant_player_list.append(self.player_buffer)
            self.player_buffer = None
        else:
            self.__move(self.player_buffer, self.connection_cell, should_reduce_move=False)

    def __move(self, player, to_cell, should_reduce_move=False):
        if should_reduce_move:
            player.reduce_remaining_moves()
        if player.get_remaining_moves() == 0:
            player.set_occupying_cell(to_cell)
        to_cell.move_in_player(player)
        self.occupant_player_list.remove(player)
