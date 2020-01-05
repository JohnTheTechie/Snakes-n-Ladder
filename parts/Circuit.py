from parts.accessor import Player


class Circuit:
    """
    Class for maintaining the circuit

    Board class have to instantiate Circuit
    A cell link map needs to be provided if a position branching is necessary
    """

    def __init__(self):
        self.__numberOfCells = 100
        self.__entryCriterion = 1
        self._maxPlayers = 0
        self._listOfPlayersOccupying = {}
        self.__cellLinkMap = {}
        print("Circuit created")

    def set_cell_link_map(self, link_map: dict):
        self.__cellLinkMap = link_map

    def set_entry_criterion(self, entry_criterion: int):
        self.__entryCriterion = entry_criterion

    def player_moves(self, player_id: Player, moves: int):
        """
        intimation to circuit about players die throw

        the circuit will evaluate if the player is present or not
            if not present, evaluated if can be added to circuit
            if present, the player shall be moved to the new position

        :param player_id: str identification of the player
        :param moves: die throw count
        :return: null
        """
        if self._check_if_player_is_an_occupant(player_id):
            new_position = self._listOfPlayersOccupying[player_id] + moves
            return self._update_player(player_id, new_position)
        elif moves == self.__entryCriterion:
            return self._add_player_to_circuit(player_id)
        else:
            return -1

    def set_maximum_number_of_players(self, number_of_players: int):
        """
        Sets the number of players actively participating

        :param number_of_players: int
        :return: null
        """
        self._maxPlayers = number_of_players

    def _check_if_player_is_an_occupant(self, player_id: Player):
        """
        check if the player is already active in the circuit

        :param player_id: str identification of the player
        :return: True if present
        """
        if player_id in self._listOfPlayersOccupying:
            return True
        else:
            return False

    def _update_player(self, player_id: Player, position: int):
        """
        Updates the players location in the circuit

        updates the location to the new calculated position
        if the new position branches to another, the same shall be updated

        :param player_id:
        :param position:
        :return: actual result position
        """
        if position <= 100:
            if position not in self.__cellLinkMap:
                self._listOfPlayersOccupying[player_id] = position
                return position
            else:
                link_position = self.__cellLinkMap[position]
                self._listOfPlayersOccupying[player_id] = link_position
                return link_position
        else:
            return self._listOfPlayersOccupying[player_id]

    def _add_player_to_circuit(self, player_id: Player):
        """
        judge if the player can be added to the circuit

        :param player_id: str identifier of player
        :return: 0 if added to the board
        """
        if len(self._listOfPlayersOccupying) >= self._maxPlayers:
            raise Exception("maximum number of players already present")
        else:
            self._listOfPlayersOccupying[player_id] = 1
            return 1
