
from gears.elements import Player
from tools.queue import Queue


class PlayerQueue:
    """
    player queue
    """
    __q: Queue

    def __init__(self, max_player_count: int = 4):
        self.__q = Queue(max_player_count)
        self.count_player = 0

    def create_player(self, name: str = None):
        player = Player(self.count_player+1, name)
        self.__q.enqueue(player)
        self.count_player += 1

    def get_next_player(self):
        player = self.__q.dequeue()
        self.__q.enqueue(player)
        return player

    def get_last_player(self):
        player = self.__q.dequeue_from_tail()
        self.__q.enqueue(player)
        return player
