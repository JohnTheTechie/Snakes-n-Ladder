import unittest
from configurations.configreader import ConfigReader as CR


class TestBase(unittest.TestCase):
    def setUp(self):
        self.reader: CR = CR()
        # self.reader.parse("/home/janakiraman/PycharmProjects/Snakes/configurations/test_game_config.xml")
        self.reader.parse()

    def tearDown(self):
        self.reader = None


class TestConfigParser(TestBase):
    def test_get_dice_type(self):
        self.assertEqual(self.reader.get_dice_type(), "dice")

    def test_get_dice_count(self):
        self.assertEqual(self.reader.get_dice_count(), 2)

    def test_get_link_list(self):
        self.assertEqual(self.reader.get_link_list(),
                         [(6, 36), (29, 75), (37, 82), (52, 98), (76, 92),
                          (99, 56), (72, 25), (69, 19), (39, 13), (26, 7)])


suite = unittest.TestLoader().loadTestsFromTestCase(TestConfigParser)
unittest.TextTestRunner(verbosity=2).run(suite)
