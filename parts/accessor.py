
class Player:

    count = 0

    def __init__(self):
        self.id_string: str = None
        self.position_in_circuit: int = None
        Player.count += 1

    @staticmethod
    def get_player_count(self):
        return Player.count

    def __del__(self):
        Player.count -= 1
        super()



