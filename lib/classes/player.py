from .result import Result

class Player:

    results_from_Result = Result.all
    all = []

    def __init__(self, username):
        self.set_username(username)
    
    def get_username(self):
        return self._username
    
    def set_username(self, username):
        if type(username) is not str:
            print("Username must be a STRING between 2 and 16 characters in length!")
        elif not (2 <= len(username) <= 16):
            print("Username must be a string between 2 and 16 characters in LENGTH!")
        else:
            print(f"Creating Player {username}!")
            self._username = username
            self.player_results_list = []
            self.add_to_player_results(self)
            self.games_played_list = []
            self.add_to_games_played()
            Player.add_to_player_list(self)
    
    username = property(get_username, set_username)

    def results(self):
        return self.player_results_list
    
    def games_played(self):
        return self.games_played_list

    @classmethod
    def add_to_player_list(cls, self):
        cls.all.append(self)
        # print(f"All Player Objects: {cls.all}")

    @classmethod
    def add_to_player_results(cls, self):
        for result in cls.results_from_Result:
            if result.player == self.username:
                self.player_results_list.append(result)
        # print(f"This players Result Instances {self.player_results_list}")
    
    # @classmethod
    # def add_to_games_played(cls, self):
    #     for result in cls.results_from_Result:
    #         if result.player == self.username:
    #             self.games_played_list.append(result.game)
        # print(f"This players games played: {self.games_played_list}")
    
    def add_to_games_played(self):
        for result in self.player_results_list:
            self.games_played_list.append(result.game)
    
    @classmethod
    def played_game(cls, self, game):
        if game in self.games_played_list:
            return True
        else:
            return False

    def num_times_played(self, game):
        num_times = 0
        for n in range(self.games_played_list):
            if game == self.games_played_list[n]:
                num_times += 1
        return num_times

    def add_result(self, game, score):
        new_result = Result(self.username, game, score)