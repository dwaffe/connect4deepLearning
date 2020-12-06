import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Flatten, Dense


class PlayerModel(tf.keras.Model):
  def __init__(self):
    super(PlayerModel, self).__init__()
    # self.input = tf.keras.Input(shape=((2, 6, 7)))
    self.conv1 = Conv2D(64, (3, 3), activation='relu', padding='same')
    # self.conv2 = Conv2D(16, (3, 3), activation='relu')
    self.flatten = Flatten()
    self.d1 = Dense(64, activation='relu')
    self.d1 = Dense(32, activation='relu')
    # self.moves_output = Dense(7, activation='softmax')
    self.position_score = Dense(1, activation='tanh')


  def call(self, x):
    # x = self.inputs(x)
    x = self.conv1(x)
    # x = self.conv2(x)
    x = self.flatten(x)
    x = self.d1(x)

    # return (self.moves_output(x), self.position_score(x))
    return self.position_score(x)
