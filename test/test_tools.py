import unittest
from parts.tools import HistoryEvent
from parts.tools import GameHistory
from parts.tools import GameHistory
from parts.tools import Dice
from parts.tools import CircularQueue
from parts.accessor import Player


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.stack1 = GameHistory()
        self.stack2 = GameHistory()

    def tearDown(self):
        self.stack1.clear_history()
        self.stack1 = None
        self.stack2 = None


class TestTools(BaseTest):
    def test_singleton(self):
        self.assertTrue(self.stack1 is self.stack2)

    def test_push(self):
        self.assertEqual(self.stack1._get_history_stack_size(), 0)
        self.stack1.push_event_to_history(HistoryEvent(0, 10, "str1"))
        self.assertEqual(self.stack1._get_history_stack_size(), 1)

    def test_clear_history(self):
        self.stack1.push_event_to_history(HistoryEvent(0, 10, "str1"))
        self.assertEqual(self.stack1._get_history_stack_size(), 1)
        self.stack1.clear_history()
        self.assertEqual(self.stack1._get_history_stack_size(), 0)

    def test_pop(self):
        self.stack1.push_event_to_history(HistoryEvent(0, 10, "str1"))
        test_event = HistoryEvent(5, 0, "str1")
        self.stack1.push_event_to_history(test_event)
        self.assertTrue(self.stack1.pop_event_from_history() is test_event)
        self.assertEqual(self.stack1._get_history_stack_size(), 1)

    def test_get_event(self):
        self.stack1.push_event_to_history(HistoryEvent(0, 10, "str1"))
        test_event = HistoryEvent(5, 0, "str1")
        self.stack1.push_event_to_history(test_event)
        self.assertTrue(self.stack1.get_last_event() is test_event)
        self.assertEqual(self.stack2._get_history_stack_size(), 2)

    def test_single_die(self):
        for x in range(1, 100):
            self.assertIn(Dice().roll(), range(1, 7))
        die = Dice()
        number = die.roll()
        self.assertEqual(number, die.last_roll)

    def test_double_die(self):
        for x in range(1, 100):
            self.assertIn(Dice(Dice.CONFIG_DOUBLE_DIE).roll(), range(2, 13))
        die = Dice()
        number = die.roll()
        self.assertEqual(number, die.last_roll)

    def test_half_set_shell_die(self):
        for x in range(1, 100):
            self.assertIn(Dice(Dice.CONFIG_HALF_SET_SHELL).roll(), [1, 2, 3, 4, 5, 6, 12])
        die = Dice()
        number = die.roll()
        self.assertEqual(number, die.last_roll)

    def test_full_set_shell_die(self):
        for x in range(1, 100):
            self.assertIn(Dice(Dice.CONFIG_FULL_SET_SHELL).roll(), range(0, 13))
        die = Dice()
        number = die.roll()
        self.assertEqual(number, die.last_roll)

    def test_queue_container(self):
        container = CircularQueue.QueueContainer(Player())
        self.assertEqual(container.turns, 1)
        container.processed(5)
        self.assertEqual(container.turns, 5)

    def test_circular_queue(self):
        que = CircularQueue()
        self.assertIs(que._focused_player, None)
        self.assertEqual(len(que._circular_queue), 0)
        self.assertEqual(que.max_player_count_limit, 2)
        que = CircularQueue(4)
        self.assertIs(que._focused_player, None)
        self.assertEqual(len(que._circular_queue), 0)
        self.assertEqual(que.max_player_count_limit, 4)

    def test_push_new_players(self):
        que = CircularQueue(3)
        que.push_new_player(Player())
        que.push_new_player(Player())
        que.push_new_player(Player())
        with self.assertRaises(Exception):
            que.push_new_player(Player())
        self.assertEqual(len(que._circular_queue), 3)


suite = unittest.TestLoader().loadTestsFromTestCase(TestTools)
unittest.TextTestRunner(verbosity=2).run(suite)
