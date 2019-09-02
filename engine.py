
import gears.Board
from gears.elements import *
from gears.elements import CellCircuit
from gears.playerQueue import PlayerQueue
import matplotlib.pyplot as plt
import logging as log

mark: Dict[Player, list]

iteration = 1
mark = {}

def print_board_status(status: dict):
    global iteration
    global mark
    log.debug(f"###############status{iteration}###############")
    for key in status.keys():
        if key not in mark.keys():
            mark[key] = []
        mark[key].append(status[key])
        log.debug(f"{key}   : {status[key]}")
    log.debug(f"######################################")
    iteration = iteration + 1


log.basicConfig(filename='example.log', level=log.DEBUG)
board = gears.Board.Board(1)
while not CellCircuit.FLAG_VICTORY:
    log.warning(f"victory reached: {CellCircuit.FLAG_VICTORY}")
    board.play_player()
    print_board_status(board.get_board_state())
for players in mark.keys():
    bar = [x for x in range(0, len(mark[players]))]
    plt.plot(bar, mark[players])

