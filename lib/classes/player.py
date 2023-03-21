# from classes.player import Player - WRONG, so I fixed it
from .result import Result

class Player:

    all = []

    def __init__(self, username):
        self.set_username(username)
    
    def get_username(self):
        return self._username
    
    def set_username(self, username):
        if (type(username) is str) and (2 <= len(username) <= 16):
            print(f"Creating Player {username}!")
            self._username = username
            self.player_results = []
            self.games_played_list = []
            Player.all.append(self)
        else:
            print("Username must be a STRING between 2 and 16 characters in LENGTH!")
    
    username = property(get_username, set_username)

    def results(self):
        self.player_results = []
        for result in Result.all:
            if result.player.username == self.username:
                self.player_results.append(result)
        return self.player_results
    
    def games_played(self):
        self.games_played_list = []
        self.results()
        for result in self.player_results:
            if result.player == self:
                self.games_played_list.append(result.game)
        return self.games_played_list

    def played_game(self, game): 
        self.games_played_list = [] 
        self.results()
        for result in self.player_results:
            if game.title in result.game.title:
                return True
        return False

    def num_times_played(self, game):
        self.games_played_list = []
        self.results()
        num_times = 0
        for result in self.player_results:
            if game.title in result.game.title:
                num_times += 1
        return num_times

    def add_result(self, game, score):
        new_result = Result(self, game, score)