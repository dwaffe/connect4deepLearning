from player.player import Player
from board.piece import Piece
import random
from board.board import Board
from connect4Logic.game import MAX_COLUMNS

class RandomPlayer(Player):
    def make_move(self, board: Board) -> int:
        return random.randint(1, MAX_COLUMNS)
        