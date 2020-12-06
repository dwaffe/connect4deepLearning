MAX_ROWS = 6
MAX_COLUMNS = 7
SIGN_PLAYER_ONE = 'X'
SIGN_PLAYER_TWO = 'O'
PLAYER_SIGNS = [SIGN_PLAYER_ONE, SIGN_PLAYER_TWO]


from connect4Logic import judge
from board.board import Board
from board.piece import Piece
from player.player import Player
from player.randomPlayer import RandomPlayer
from typing import Optional
import numpy as np


class Game:
    def __init__(self, player_one: Player = None, player_two: Player = None, verbose: bool = True) -> None:
        self._move_counter = 0
        self._board = Board(MAX_ROWS, MAX_COLUMNS)
        self._players = (
            player_one if player_one is not None else Player(
                SIGN_PLAYER_ONE, 'magenta'),
            player_two if player_two is not None else Player(
                SIGN_PLAYER_TWO, 'cyan')
        )
        self._verbose = verbose

# WHY Optional[tuple[list, int]] DID NOT WORK? 
    def run(self, return_log_boards: bool = False) -> Optional[tuple]:
        board_log = []
        while(judge.is_game_over(self._board) is not True):
            current_player = self._players[self._move_counter % 2]
            self._print(self._board)
            self._print(' 1  2  3  4  5  6  7')

            move = current_player.make_move(self._board) - 1

            if judge.is_valid_move(self._board, move) is not True:
                self._print('bad move!')
                continue

            self.make_move(current_player, move)

            if return_log_boards == True:
                board_log.append(self._board.get_array_by_signs(PLAYER_SIGNS))

            self._move_counter += 1

        self._print(self._board)
        board_log = np.array(board_log)

        if judge.is_winning(self._board, SIGN_PLAYER_ONE):
            self._print('{} is a winner!'.format(SIGN_PLAYER_ONE))
            return (board_log, 1)

        elif judge.is_winning(self._board, SIGN_PLAYER_TWO):
            self._print('{} is a winner!'.format(SIGN_PLAYER_TWO))
            return (board_log, -1)

        else:
            self._print('Draw')
            return (board_log, 0)


    def make_move(self, player: Player, column: int):
        for row in reversed(range(MAX_ROWS)):
            if self._board.is_empty(column, row):
                self._board.put_piece(column, row, player.get_piece())
                return


    def _print(self, text: str):
        if self._verbose == True:
            print(text)
