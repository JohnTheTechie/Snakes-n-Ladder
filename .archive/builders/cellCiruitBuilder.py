
import Elements.Cell as cell
from Configurations.cell_config import CellConfig
from Elements.board import Board
from Elements.Cell import Cell


class CircuitBuilder:

    @staticmethod
    def build():
        return CircuitBuilder.__create_circuit()

    @staticmethod
    def __create_circuit():
        first_cell = CircuitBuilder.__create_cell()
        last_cell = first_cell
        for count in range(2, CellConfig.get_cell_count()):
            temp = CircuitBuilder.__create_cell(count)
            temp.previous_cell, last_cell = last_cell, temp
        return first_cell, last_cell

    @staticmethod
    def __create_cell(index=0):
        temp = Cell()
        temp.index = index
        return temp

    @staticmethod
    def __assign_rolls(first_cell):
        for fro,to in CellConfig.get_ladders():
            cell = CircuitBuilder.__get_cell_by_index(first_cell, fro)
            cell.connection_cell = CircuitBuilder.__get_cell_by_index(first_cell, to)
            cell.kind = CellConfig.get_ladder_id()
        for fro,to in CellConfig.get_snakes():
            cell = CircuitBuilder.__get_cell_by_index(first_cell, fro)
            cell.connection_cell = CircuitBuilder.__get_cell_by_index(first_cell, to)
            cell.kind = CellConfig.get_snakes_id()

    @staticmethod
    def __get_cell_by_index(first_cell, id):
        cell = first_cell
        while cell.index != id:
            cell = cell.next_cell
        return cell




