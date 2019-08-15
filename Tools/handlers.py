
class Queue:


    class EmptyQueueError(Exception):
        """
        raisd when dequeue is requested on an empty queue
        The model here is enqueue from right, deque from left.
        Bidirectional access allowed with l_enqueue, r_dequeue
        """

        def __init__(self, message, caller=None):
            self.message = message
            self.caller = caller

    __count = 0

    def __init__(self, name=""):
        Queue.__count += 1
        if name.__eq__(""):
            self.__name =  "queue_"+str(Queue.__count)
        self.__name = name
        self.__q = []

    def enqueue(self, obj):
        self.__q.append(obj)

    def l_enqueue(self, obj):
        self.__q.insert(0, obj)

    def dequeue(self):
        if Queue.__count == 0:
            raise Queue.EmptyQueueError()
        return self.__q.pop(0)

    def r_dequeue(self):
        if Queue.__count == 0:
            raise Queue.EmptyQueueError()
        return self.__q.pop()

    def size(self):
        return len(self.__q)



