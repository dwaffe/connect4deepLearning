from AI.player_model import PlayerModel
from AI.self_play import play_games
import tensorflow as tf
import numpy as np
from connect4Logic.game import Game, SIGN_PLAYER_ONE, SIGN_PLAYER_TWO
from player.ai_player import AIPlayer
from player.player import Player
import random


model = PlayerModel()
model.compile(tf.keras.optimizers.Adam(learning_rate=1e-3), tf.keras.losses.MeanSquaredError())


for x in range(40):
  boards, labels = play_games(150, model)
  indices = np.arange(labels.shape[0])
  np.random.shuffle(indices)

  boards = boards[indices]
  labels = labels[indices]
  model.fit(boards, labels, validation_split=0, epochs=2)

game = Game(AIPlayer(SIGN_PLAYER_ONE, 'magenta', model), Player(SIGN_PLAYER_TWO, 'cyan'))
game.run()







# save or not to save? 
# f = h5py.File("games_log.hdf5", "w")

# input()
