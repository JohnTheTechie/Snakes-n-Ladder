
SIZE_EMPTY_STACK = 0

class Stack:
    """
    Simple implementation of the Stack data structure
    """

    def __init__(self):
        self.__stack = []

    def push(self, item):
        """
        push item into the stack
        :param item: _T
        :return: None
        """
        self.__stack.append(item)

    def pop(self):
        """
        Pop the item from the stack
        :return: _T
        """
        if len(self.__stack) == SIZE_EMPTY_STACK:
            raise Exception
        return self.__stack.pop()

    def get_size(self):
        """
        return the size of the stack
        :return: int size of stack
        """
        return len(self.__stack)

