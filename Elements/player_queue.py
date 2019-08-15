from Tools import handlers
from Configurations import numbers
import Elements.player

class PlayerQueue:

    player_queue = None

    def __init__(self):
        self.__make_player_set()

    def __new__(cls, *args, **kwargs):
        if cls.player_queue is None:
            cls.player_queue = PlayerQueue()
        return cls.player_queue

    def __make_player_set(self):
        self.__queue = handlers.Queue("Player Queue")
        for num in range(1, numbers.Board.Count_Player+1):
            temp_player = Elements.player.Player(num)
            self.__queue.enqueue(temp_player)

    def get_next_player(self):
        temp = self.__queue.dequeue()
        self.__queue.enqueue(temp)
        return temp

    def get_the_last_player_again(self):
        temp = self.__queue.r_dequeue()
        self.__queue.enqueue(temp)
        return temp

