MAX_ROWS = 6
MAX_COLUMNS = 7

from player.randomPlayer import RandomPlayer
from player.player import Player
from board.piece import Piece
from board.board import Board
from connect4Logic import judge


class Game:
    def __init__(self, verbose = True) -> None:
        self._move_counter = 0
        self._board = Board(MAX_ROWS, MAX_COLUMNS)
        self._players = (Player('X', 'magenta'), Player('O', 'cyan'))
        # self._players = (RandomPlayer('X', 'magenta'), RandomPlayer('O', 'cyan'))
        self._verbose = verbose


    def run(self):
        while(judge.is_game_over(self._board) is not True):
            current_player = self._players[self._move_counter % 2]
            self._print(self._board)
            self._print(' 1  2  3  4  5  6  7')

            move = current_player.make_move() - 1

            if judge.is_valid_move(self._board, move) is not True:
                self._print('bad move!')
                continue

            self.make_move(current_player, move)
            self._move_counter += 1
        
        self._print(self._board)

        if judge.is_winning(self._board, 'X'):
            self._print('X is a winner!')
        elif judge.is_winning(self._board, 'O'):
            self._print('O is a winner!')
        else:
            self._print('Draw')

            
    def make_move(self, player: Player, column: int):
        for row in reversed(range(MAX_ROWS)):
            if self._board.is_empty(column, row):
                self._board.put_piece(column, row, player.get_piece())
                return

    
    def _print(self, text: str):
        if self._verbose == True:
            print(text)