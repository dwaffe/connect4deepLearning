from player.player import Player
from board.piece import Piece
from board.board import Board
import random
from connect4Logic.game import MAX_COLUMNS, MAX_ROWS, PLAYER_SIGNS
from tensorflow.keras import Model
import copy
import numpy as np

class AIPlayer(Player):
    def __init__(self, sign: str, color: str, model: Model, random_moves: bool = False) -> None:
        super().__init__(sign, color)
        self._model = model
        self._random_moves = random_moves


    def make_move(self, board: Board) -> int:
        players_signs = copy.copy(PLAYER_SIGNS)
        players_signs.remove(self._piece.get_sign())
        players_signs.insert(0, self._piece.get_sign())
        
        moves = range(MAX_COLUMNS)
        moves_score = np.zeros(MAX_COLUMNS)
        temp_boards_to_score = [None] * MAX_COLUMNS

        for move in moves:
            temp_board = copy.deepcopy(board)
            for row in reversed(range(MAX_ROWS)):
                if temp_board.is_empty(move, row):
                    temp_board.put_piece(move, row, self.get_piece())
                    
                    temp_boards_to_score[move] = temp_board.get_array_by_signs(players_signs)
                    break

        
        boards_to_score = []
        moves_translator = dict()
        move_index = 0

        for idx, board in enumerate(temp_boards_to_score):
            if board is None:
                continue
            else:
                boards_to_score.append(board)
                moves_translator[move_index] = idx + 1
                move_index += 1
                
        # print(boards_to_score)
        boards_to_score = np.array(boards_to_score)
        
        scores = self._model.predict(boards_to_score)
        
        if self._random_moves == True:
            max_possible_moves = min([len(scores), 3])
            return moves_translator[random.choice(np.argpartition(np.squeeze(scores),-max_possible_moves)[-max_possible_moves:])]
        else:
            return moves_translator[np.argmax(scores)]

          
            

        
        # self._model.predict()
        # todo: może by tablica sama zwracała wszystkie tablice (dla X i O) 
        # y = self._model([board.get_array('X'), board.get_array('O')]) 
        # print(board.get_array('X'))
        # print(board.get_array_by_signs(['X', 'O']))
    
        return random.randint(1, MAX_COLUMNS)
        