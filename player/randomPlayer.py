from player.player import Player
from board.piece import Piece
import random
from connect4Logic.game import MAX_COLUMNS

class RandomPlayer(Player):
    def make_move(board) -> int:
        return random.randint(1, MAX_COLUMNS)
        