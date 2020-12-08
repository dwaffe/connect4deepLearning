from connect4Logic.game import MAX_ROWS, MAX_COLUMNS, SIGN_PLAYER_ONE, SIGN_PLAYER_TWO
from board.board import Board
import numpy as np
from scipy.signal import convolve2d


horizontal_kernel = np.array([[1, 1, 1, 1]])
vertical_kernel = np.transpose(horizontal_kernel)
diag1_kernel = np.eye(4, dtype=np.uint8)
diag2_kernel = np.fliplr(diag1_kernel)
kernels = [horizontal_kernel, vertical_kernel, diag1_kernel, diag2_kernel]


def is_valid_move(board: Board, move: int) -> bool:
    try:
        return board.is_empty(move, 0)
    except IndexError:
        return False


def is_game_over(board: Board) -> bool:
    if is_winning(board, SIGN_PLAYER_ONE) or is_winning(board, SIGN_PLAYER_TWO) or is_board_is_full(board):
        return True


def is_board_is_full(board: Board) -> bool:
    if board.get_move_counter() < 42: 
        return False

    return True


def is_winning(board: Board, sign: str) -> bool:
    if board.get_move_counter() < 7: 
        return False

    board = board.get_array(sign)
    for kernel in kernels:
        if (convolve2d(board, kernel, mode='valid') == 4).any():
            return True
    return False
