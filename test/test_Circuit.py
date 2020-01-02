import unittest
from parts.Circuit import Circuit


class TestCircuit(unittest.TestCase):

    player = "pl1"
    false_player = "pl2"

    def test_player_presence(self):
        circuit = Circuit()
        circuit._listOfPlayersOccupying[TestCircuit.player] = 10
        self.assertTrue(circuit._check_if_player_is_an_occupant(TestCircuit.player))
        self.assertFalse(circuit._check_if_player_is_an_occupant(TestCircuit.false_player))

    def test_update_non_existing_player(self):
        circuit = Circuit()
        self.assertEqual(circuit.player_moves(TestCircuit.player, 10), -1)

    def test_max_count(self):
        circuit = Circuit()
        with self.assertRaises(Exception):
            circuit.player_moves(TestCircuit.player, 1)

    def test_entryCondition(self):
        circuit = Circuit()
        circuit.set_maximum_number_of_players(2)
        self.assertEqual(circuit.player_moves(TestCircuit.player, 1), 1)

    def test_update_existing_player(self):
        circuit = Circuit()
        circuit.set_maximum_number_of_players(2)
        circuit.player_moves(TestCircuit.player, 1)
        self.assertEqual(circuit.player_moves(TestCircuit.player, 10), 11)

    def test_branching(self):
        circuit = Circuit()
        circuit.set_cell_link_map({10: 25})
        circuit.set_maximum_number_of_players(2)
        circuit.player_moves(TestCircuit.player, 1)
        self.assertEqual(circuit.player_moves(TestCircuit.player, 9), 25)

    def test_circuit_boundary(self):
        circuit = Circuit()
        circuit.set_maximum_number_of_players(2)
        circuit.player_moves(TestCircuit.player, 1)
        circuit.player_moves(TestCircuit.player, 95)
        self.assertEqual(circuit.player_moves(TestCircuit.player, 5), 96)
        self.assertEqual(circuit.player_moves(TestCircuit.player, 1), 97)
        self.assertEqual(circuit.player_moves(TestCircuit.player, 3), 100)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCircuit)
unittest.TextTestRunner(verbosity=2).run(suite)
