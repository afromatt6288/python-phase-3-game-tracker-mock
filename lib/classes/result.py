class Result:

    all =[]

    def __init__(self, player, game, score = 0):
        self.player = player
        self.game = game
        # self.set_player(player)
        # self.set_game(game)
        self.set_score(score)
        Result.all.append(self)

    # def get_player(self):
    #     return self._player

    # def set_player(self, player):
    #     self._player = player
    
    # player = property(get_player, set_player)

    # def get_game(self):
    #     return self._game

    # def set_game(self, game):
    #     self._game = game
    
    # game = property(get_game, set_game)
    
    def get_score(self):
        return self._score

    def set_score(self, score):
        if (type(score) is int) and (1 <= score <= 5000):
            self._score = score
    
    score = property(get_score, set_score)