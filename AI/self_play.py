from re import T
from tensorflow.python.keras.engine.training import Model
from connect4Logic.game import Game, SIGN_PLAYER_ONE, SIGN_PLAYER_TWO
from player.ai_player import AIPlayer
from player.randomPlayer import RandomPlayer
from AI.player_model import PlayerModel
import numpy as np


def play_games(numer_of_games: int = 10, model: Model = PlayerModel()) -> np.array:

    board_log = []
    label = []
    AI_win_count = 0
    for i in range(numer_of_games):
        playerOne = AIPlayer(SIGN_PLAYER_ONE, 'magenta', model, True)
        playerTwo = AIPlayer(SIGN_PLAYER_TWO, 'cyan', model, True)
        # if i % 2 == 0:
        #     playerOne = AIPlayer(SIGN_PLAYER_ONE, 'magenta', model)
        #     playerTwo = RandomPlayer(SIGN_PLAYER_TWO, 'cyan')
        # else:
        #     playerOne = RandomPlayer(SIGN_PLAYER_TWO, 'cyan')
        #     playerTwo = AIPlayer(SIGN_PLAYER_ONE, 'magenta', model)

        # print(i)
        # game = Game(RandomPlayer(SIGN_PLAYER_ONE, 'magenta'), RandomPlayer(SIGN_PLAYER_TWO, 'cyan'), verbose = False)
        game = Game(playerOne, playerTwo, verbose = False)
        game_log, score = game.run(return_log_boards=True)
        if i % 2 == 0 and score == 1:
            AI_win_count += 1

        if i % 2 != 0 and score == -1:
            AI_win_count += 1
            

        for board in game_log:
            board_log.append(board)
            label.append(score)
    
    print('AI wins ' + str(AI_win_count))
    return np.array(board_log, dtype=np.float32), np.array(label, dtype=np.float32)

