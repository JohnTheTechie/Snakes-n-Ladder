import unittest
from parts.Circuit import Circuit
from parts.exceptions import *
from parts.tools import Dice, GameHistory, CircularQueue, HistoryEvent
from parts.accessor import Player
from configurations.configreader import ConfigReader as CR
from arena import Arena


class TestArena(unittest.TestCase):
    def test_exceptions(self):
        arena = Arena()
        with self.assertRaises(IllegalStateException):
            arena._set_dice("fuil", 2)
            arena.get_player_set()
            arena.get_dice_roll()

    def test_roll_events(self):
        arena: Arena = Arena()
        arena.prepare_arena()
        player_list = arena.get_player_set()
        event_trigger_list = [2, 1,
                              6, 5,
                              1, 1,
                              5, 1,
                              5, 6,
                              1, 5,
                              1, 5]
        for roll in event_trigger_list:
            arena.roll_event_triggered(roll)
        self.assertEqual(player_list[0].position_in_circuit, 43)
        self.assertEqual(player_list[1].position_in_circuit, 56)


if __name__ == '__main__':
    unittest.main()
