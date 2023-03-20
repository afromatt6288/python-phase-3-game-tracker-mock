# class Player:
#     def __init__(self, player):
#         self.player = player

# class Game:
#     def __init__(self, game):
#         self.game = game

class Result:

    all =[]

    def __init__(self, player, game, score = 0):
        self.set_player(player)
        # self.player = isinstance(player, Player)
        self.set_game(game)
        # self.game = isinstance(game, Game)
        self.score = score
        Result.add_to_result_list(self)

    def get_player(self):
        return self._player

    def set_player(self, player):
        # if not isinstance(player, Player):
        #     raise ValueError("player must be an instance of the Player class")
    #     print(f"Creating Player: {player}!")
        self._player = player
    
    player = property(get_player, set_player)

    def get_game(self):
        return self._game

    def set_game(self, game):
        # if not isinstance(game, Game):
        #     raise ValueError("game must be an instance of the Game class")
    #     print(f"Creating Game: {game}!")
        self._game = game
    
    game = property(get_game, set_game)
    
    def get_score(self):
        return self._score

    def set_score(self, score):
    #     if type(score) is not int:
    #         print("Score must be a NUMBER between 1 and 5000!")
    #     elif not (1 <= len(score) <= 5000):
    #         print("Score must be a number BETWEEN 1 and 5000!")
    #     else:
    #         print(f"Creating Score: {score}!")
                # self._score = score
        if (type(score) is int) and (1 <= score <= 5000):
            self._score = score
    
    score = property(get_score, set_score)

    @classmethod
    def add_to_result_list(cls, self):
        cls.all.append(self)
        print(cls.all)


# result_1 = Result('Tricia', "Skribbl.io", 3000)
# result_2 = Result('Bianca', "Skribbl.io", 3000)
# result_3 = Result('Tricia', "Bobble.io", 3000)
# result_4 = Result('Bianca', "Bobble.io", 3000)