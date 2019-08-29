
import random
import logging

class Dice:

    dice = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.dice is None:
            cls.dice = Dice()
            logging.info(f"{cls.dice} created anew")
        logging.info(f"{cls.dice} returned")
        return cls.dice

    def roll(self):
        temp = random.randint(1, 6)
        return temp

    def __str__(self):
        temp = "Dice singleton element"
        return self.dice




