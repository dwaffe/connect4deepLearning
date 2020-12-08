from board.piece import Piece
from board.field import Field
import numpy as np


class Board:
    def __init__(self, rows: int, columns: int) -> None:
        self._rows = rows
        self._columns = columns
        self._board = [[Field() for i in range(columns)] for j in range(rows)]
        self._move_counter = 0
        

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
        self._move_counter += 1


    def is_empty(self, column_index: int, row_index: int) -> bool:
        return self._board[row_index][column_index].get_piece() is None


    def get_array(self, sign: str) -> np.array:
        return np.array([[int(field.is_sign(sign)) for field in row] for row in self._board], dtype=np.float32)


    def get_array_by_signs(self, signs: list) -> np.array:
        return np.stack((self.get_array(sign) for sign in signs))


    def get_move_counter(self) -> int:
        return self._move_counter

