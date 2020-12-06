from board.piece import Piece
import random
from connect4Logic.game import MAX_COLUMNS

class Player:
    def __init__(self, sign: str, color: str) -> None:
        self._piece = Piece(sign, color)


    def make_move(board) -> int:
        while True:
            try: 
                return int(input('Make move: '))
            except ValueError:
                continue


    def get_piece(self) -> str:
        return self._piece