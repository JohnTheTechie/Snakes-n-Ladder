

class CellConfig:
    ladders = [(18, 37), (12, 64), (40, 58), (53, 69), (51, 95), (62, 85)]
    snakes = [(98, 66), (80, 43), (87, 57), (54, 17), (50, 27), (25, 6)]
    ladders_id = "ladder"
    snakes_id = "snake"
    cell_count = 100

    @staticmethod
    def get_ladders():
        return CellConfig.ladders

    @staticmethod
    def get_snakes():
        return CellConfig.snakes_id

    @staticmethod
    def get_ladder_id():
        return CellConfig.ladders_id

    @staticmethod
    def get_snakes_id():
        return CellConfig.snakes_id

    @staticmethod
    def get_cell_count():
        return CellConfig.cell_count