from .piece import Piece
from typing import Optional
from colorama import init
from termcolor import colored


init()


class Field:
    def __init__(self, piece: Optional[Piece] = None) -> None:
        self._piece = piece

    def get_piece(self) -> Optional[Piece]:
        return self._piece

    def put_piece(self, piece: Piece):
        self._piece = piece

    def __str__(self) -> str:
        if self._piece is not None:
            return colored(self._piece.get_sign(), self._piece.get_color())
        else:
            return ' '
    
    def is_sign(self, sign: str):
        if self._piece is None:
            return False
        
        return self._piece.get_sign() == sign