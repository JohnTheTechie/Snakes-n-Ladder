import parts.exceptions as EXC
import random
from parts.accessor import Player


class HistoryEvent:
    """
    class for holding an event in the board
    """

    def __init__(self, from_index: int, to_index: int, player):
        self.from_cell = from_index
        self.to_cell = to_index
        self.player = player


class GameHistory:
    """
    Maintains history across the project
    """

    'constants'
    __HISTORY_STACK_EMPTY = 0
    'singleton reference'
    __history = None

    def __init__(self):
        self.__stack = []
        self.b = 0

    def __new__(cls, *args, **kwargs):
        if cls.__history is None:
            cls.__history = object.__new__(cls)
        return cls.__history

    def push_event_to_history(self, event: HistoryEvent):
        """
        adds the event to the history stack

        :param event:
        :return: None
        """
        self.__stack.append(event)

    def pop_event_from_history(self):
        """
        retrieve and remove the last event from the stack

        :return: last event: HistoryElement
        """
        if self._get_history_stack_size() == GameHistory.__HISTORY_STACK_EMPTY:
            raise EXC.HistoryUnderflowException()
        else:
            return self.__stack.pop()

    def get_last_event(self):
        """
        retrieve the last event from the stack

        :return: last event: HistoryElement
        """
        if self._get_history_stack_size() == GameHistory.__HISTORY_STACK_EMPTY:
            raise EXC.HistoryUnderflowException()
        else:
            return self.__stack[len(self.__stack)-1]

    def clear_history(self):
        """
        resets the history stack
        
        :return: None
        """
        self.__stack = []

    def _get_history_stack_size(self):
        return len(self.__stack)


class Dice:
    """
    class implementing Game dice behaviour
    """

    CONFIG_SINGLE_DIE = {"low": 1, "high": 6}
    CONFIG_DOUBLE_DIE = {"low": 2, "high": 12}
    CONFIG_HALF_SET_SHELL = {"low": 1, "high": 7}
    CONFIG_FULL_SET_SHELL = {"low": 0, "high": 12}

    def __init__(self, config: dict = CONFIG_SINGLE_DIE):
        self.last_roll = None
        self.__die_config = config

    def roll(self):
        """
        generates a random number within the range specified by the dice type selected

        :return: random number within dice range
        """
        self.last_roll = random.randint(self.__die_config["low"], self.__die_config["high"])
        if self.__die_config is Dice.CONFIG_HALF_SET_SHELL and self.last_roll == 7:
            self.last_roll = 12
        return self.last_roll


class CircularQueue:
    """
    Queue for maintaining player list
    """

    class QueueContainer:
        """
        Container for PlayerQueue
        """

        def __init__(self, player: Player, turns: int = 1):
            self.player = player
            self.turns = turns

        def processed(self, bonus_turns: int = 0):
            """
            adjusts the turn counter as per game play
            :param bonus_turns:
            :return: None
            """
            self.turns = self.turns - 1 + bonus_turns

    def __init__(self, max_players_in_game: int = 2):
        """
        Initializes the queue
        :param max_players_in_game: default 2
        """
        self.max_player_count_limit = max_players_in_game
        self._circular_queue = []
        self._focused_player: CircularQueue.QueueContainer = None
        self._pending_transaction = False

    def __enqueue(self, container: QueueContainer):
        """
        pushes the encapsulated player into the queue

        if the max size already reached, raises a Overflow Exception
        :param container:
        :return: None
        """
        if len(self._circular_queue) >= self.max_player_count_limit:
            raise EXC.PlayerQueueOverflowException("max player size already present")
        self._circular_queue.insert(0, container)

    def __pseudo_dequeue(self):
        """
        fetch the player with next turn

        if the queue is empty raises underflow exception
        if pending transaction flag is set, raises illegal state exception
        else stores reference to focused_player variable and returns the same

        :return:None
        """
        if len(self._circular_queue) == 0:
            raise EXC.PlayerQueueUnderFlowException("Dequeue performed on an empty queue")
        elif self._pending_transaction:
            raise EXC.IllegalStateException("pending transaction not completed")
        else:
            self._focused_player = self._circular_queue[len(self._circular_queue) - 1]
            self._pending_transaction = True
            return self._focused_player

    def __dequeue(self):
        """
        removes the turn less container to the end of the queue

        if queue is empty throws PlayerQueueUnderFlowException
        if pending flag is set, throw IllegalStateException
        else pushes the turnless container to the end
        :return:
        """
        if len(self._circular_queue) == 0:
            raise EXC.PlayerQueueUnderFlowException("Dequeue performed on an empty queue")
        elif self._pending_transaction:
            raise EXC.IllegalStateException("pending transaction not completed")
        elif self._focused_player.turns == 0:
            self._focused_player.turns = 1
            container = self._circular_queue.pop()
            self._circular_queue.insert(0, container)

    def push_new_player(self, player: Player, turns: int = 1):
        """
        pushes the player encapsulated in Container to the Queue

        :param turns:
        :param player:
        :return:
        """
        container = CircularQueue.QueueContainer(player, turns)
        self.__enqueue(container)

    def get_next_player(self):
        """
        get the next player with turns

        :return: Player
        """
        if len(self._circular_queue) == 0:
            raise EXC.PlayerQueueUnderFlowException("player queue is tried to be accessed when empty")
        return self.__pseudo_dequeue()

    def complete_transaction(self, bonus_turns: int = 0):
        """
        resets the pending flag and reduces the turn count

        :param bonus_turns:
        :return:
        """
        if self._focused_player is None:
            raise EXC.NullPointerException("focused player is pointing to Null")
        self._focused_player.processed(bonus_turns)
        self._pending_transaction = False
        self.__dequeue()
