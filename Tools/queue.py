
QUEUE_FIRST_INDEX = 0
QUEUE_LAST_INDEX = -1
SIZE_EMPTY_QUEUE = 0


class Queue:
    """
    simple implemetation of Bidirectional Queue data structure
    """

    def __init__(self, max_size=None):
        """
        create a queue
        if queue size is to be limited, max_size needs to be initialized
        :param max_size:
        """
        self.__q = []
        self.__max_size = max_size

    def enqueue(self, item):
        """
        add the item to the end of the queue
        :param item: _T
        :return: size of the queue
        """
        self.__q.append(item)
        if self.__max_size is not None and len(self.__q) > self.__max_size:
            raise Exception
        return len(self.__q)

    def enqueue_at_mouth(self, item):
        """
        add the item to the mouth of the queue
        :param item: _T
        :return: size of the queue
        """
        self.__q.insert(QUEUE_FIRST_INDEX, item)
        if self.__max_size is not None and len(self.__q) > self.__max_size:
            raise Exception
        return len(self.__q)

    def dequeue(self):
        """
        pull out the item from the mouth of the queue
        :return: size of the queue
        """
        if len(self.__q) == SIZE_EMPTY_QUEUE:
            raise Exception
        else:
            temp = self.__q[QUEUE_FIRST_INDEX]
            self.__q.remove(temp)
            return temp

    def dequeue_from_tail(self):
        """
        pull out the item from the end of the queue
        :return: size of the queue
        """
        if len(self.__q) == SIZE_EMPTY_QUEUE:
            raise Exception
        else:
            temp = self.__q[QUEUE_LAST_INDEX]
            self.__q.remove(temp)
            return temp
