from connect4Logic.game import Game
from player.randomPlayer import RandomPlayer
import time


start_time = time.time()
seconds = 3
playout_count = 0

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    game = Game(RandomPlayer('X'), RandomPlayer('O'), verbose=False)
    game.run()
    playout_count += 1

    if elapsed_time > seconds:
        print("Finished iterating in: " + str(elapsed_time)  + " seconds")
        print("Played games: " + str(playout_count))
        break

