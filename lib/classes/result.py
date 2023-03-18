class Result:

    all =[]

    def __init__(self, player, game, score = 0):
        self.player = player
        self.game = game
        self.score = score
        Result.add_to_result_list(self)

    # def get_player(self):
    #     return self._player

    # def set_player(self, player):
    #     print(f"Creating Player: {player}!")
    #     self._player = player
    
    # player = property(get_player, set_player)

    # def get_game(self):
    #     return self._game

    # def set_game(self, game):
    #     print(f"Creating Game: {game}!")
    #     self._game = game
    
    # game = property(get_game, set_game)
    
    # def get_score(self):
    #     return self._score

    # def set_score(self, score):
    #     if type(score) is not int:
    #         print("Score must be a NUMBER between 1 and 5000!")
    #     elif not (1 <= len(score) <= 5000):
    #         print("Score must be a number BETWEEN 1 and 5000!")
    #     else:
    #         print(f"Creating Score: {score}!")
    #         self._score = score
    
    # score = property(get_score, set_score)

    @classmethod
    def add_to_result_list(cls, self):
        cls.all.append(self)
        print(cls.all)
