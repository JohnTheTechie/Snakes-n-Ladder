from parts.Circuit import Circuit
from parts.exceptions import *
from parts.tools import Dice, GameHistory, CircularQueue, HistoryEvent
from parts.accessor import Player
from configurations.configreader import ConfigReader as CR


class Arena:

    def __init__(self):
        self.game_name = "Snakes"
        self.dice: Dice = None
        self.configs: CR = CR()
        self.configs.parse()
        self.history: GameHistory = None
        self.player_queue: CircularQueue = None
        self.player_count = 2
        self.circuit = None
        self.player_set = []

    def prepare_arena(self):
        """
        Instantiate and initialize all tools

        :return: None
        """
        self._set_dice(self.configs.get_dice_type(), self.configs.get_dice_count())
        self.history = GameHistory()
        self._create_player_list()
        self._set_player_queue(self.player_set, self.player_count)
        self._set_circuit()
        self.circuit.set_entry_criterion(1)
        self._set_link_map(self.configs.get_link_list())

    def _set_dice(self, dice_type, dice_count):
        if dice_type == "dice" and dice_count == 1:
            self.dice = Dice(Dice.CONFIG_SINGLE_DIE)
        elif dice_type == "dice" and dice_count == 2:
            self.dice = Dice(Dice.CONFIG_DOUBLE_DIE)
        elif dice_type == "shell" and dice_count == 1:
            self.dice = Dice(Dice.CONFIG_HALF_SET_SHELL)
        elif dice_type == "shell" and dice_count == 2:
            self.dice = Dice(Dice.CONFIG_FULL_SET_SHELL)
        else:
            raise IllegalStateException("Undefined dice behaviour configured")

    def _set_player_queue(self, player_list, max_player_count=2):
        self.player_queue = CircularQueue(max_player_count)
        for player in player_list:
            self.player_queue.push_new_player(player)

    def _set_circuit(self, max_player_count=2):
        self.circuit = Circuit()
        self.circuit.set_maximum_number_of_players(max_player_count)

    def _create_player_list(self, player_count=2):
        for n in range(0, player_count):
            self.player_set.append(Player())

    def _set_link_map(self, link_map: list):
        link_map_dict = {}
        for x, y in link_map:
            link_map_dict[x] = y
        self.circuit.set_cell_link_map(link_map_dict)

    def get_last_roll(self):
        """
        reads the roll value from the previous roll

        :return: last roll value
        """
        if self.dice is None:
            raise IllegalStateException("dice is not et created")
        if self.dice.last_roll is None:
            raise IllegalStateException("dice not rolled yet")
        return self.dice.last_roll

    def get_dice_roll(self):
        """
        rolls the dice and returns the value

        :return:
        """
        if self.dice is None:
            raise IllegalStateException("dice is not et created")
        if self.dice.last_roll is None:
            raise IllegalStateException("dice not rolled yet")
        return self.dice.roll()

    def roll_event_triggered(self, count: int):
        """
        triggers roll event

        receives the dice roll
        gets the current player from queue and assigns new position
        and pushes the player back to the queue

        creates a history event and pushes it into the history stack

        :return: None
        """
        current_player: CircularQueue.QueueContainer = self.player_queue.get_next_player()

        old_position = current_player.player.position_in_circuit
        new_position = self.circuit.player_moves(current_player.player, count)
        current_player.player.position_in_circuit = new_position

        self.player_queue.complete_transaction()

        event = HistoryEvent(old_position, new_position, current_player)
        self.history.push_event_to_history(event)

    def get_player_set(self):
        """
        called by HMI to get reference of all player objects

        :return: [players... ]
        """
        if len(self.player_set) == 0:
            raise IllegalStateException("player set not yet prepared")
        return self.player_set
