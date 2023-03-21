#!/usr/bin/env python3
# import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")



game = Game("Skribbl.io")
game_2 = Game("Scattegories")
game_3 = Game("Codenames")


player = Player('Saaammmm')
player_2 = Player('ActuallyTopher')
player_3 = Player('Nick')
player_4 = Player('Ari')


result_1 = Result(player, game, 2000)
result_2 = Result(player_2, game_2, 3500)
result_3 = Result(player_3, game_3, 190)
result_4 = Result(player_4, game, 5000)
result_5 = Result(player, game_2, 4999)
result_6 = Result(player_2, game_3, 5000)
result_7 = Result(player_3, game, 4999)
result_8 = Result(player_4, game_2, 5000)
result_9 = Result(player, game_3, 19)
result_10 = Result(player_2, game_3, 10)
result_11 = Result(player_3, game_2, 190)
result_12 = Result(player_4, game_3, 5000)


player.played_game(game)

    # ipdb.set_trace()
