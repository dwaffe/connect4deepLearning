from board.piece import Piece
from board.field import Field
import numpy as np


class Board:
    def __init__(self, rows: int, columns: int) -> None:
        self._rows = rows
        self._columns = columns
        self._board = [[Field() for i in range(columns)] for j in range(rows)]
        

    def print(self):
        print(self.__str__())


    def __str__(self) -> str:
        string_board = ''
        for column in self._board:
            string_board += '\n'
            for field in column:
                string_board += '[' + str(field) + ']'

        return string_board


    def put_piece(self, column_index: int, row_index: int, piece: Piece):
        self._board[row_index][column_index].put_piece(piece)


    def is_empty(self, column_index: int, row_index: int) -> bool:
        return self._board[row_index][column_index].get_piece() is None


    def get_array(self, sign: str):
        return np.array([[int(field.is_sign(sign)) for field in row] for row in self._board])


