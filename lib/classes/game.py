from .result import Result

class Game:

    results_from_Result = Result.all
    all = []

    def __init__(self, title):
        self.set_title(title)
    
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if hasattr(self, "_title"):
            print("Cannot change Game Title!")
        elif type(title) is not str:
            print("Title must be a STRING longer than 0 characters.")
        elif len(title) == 0:
            print("Title must be a string LONGER than 0 characters.")
        # elif self.check_title(title):
        #     print(f"Game already exists!")
        else:
            print(f"Creating Game {title}!")
            self._title = title
            self.game_results = []
            self.add_to_game_results(self)
            self.players_list = []
            self.add_to_players_list()
            Game.add_to_game_list(self)
    
    title = property(get_title, set_title)

    def results(self):
        return self.game_results
    
    def players(self):
        return self.players_list

    @classmethod
    def check_title(cls, title):
        for game in cls.all:
            if title == game.title:
                return True
        return False
    
    @classmethod
    def add_to_game_list(cls, self):
        cls.all.append(self)
        print(cls.all)

    @classmethod
    def add_to_game_results(cls, self):
        for result in cls.results_from_Result:
            if result.game == self.title:
                self.game_results.append(result)
    
    def add_to_players_list(self):
        for result in self.game_results:
            self.players_list.append(result.player)
    
    def average_score(self, player):
        avg_score = 0
        game_num = 0
        for result in self.game_results:
            if result.player == player:
                avg_score += result.score
                game_num += 1
        if game_num != 0:
            return avg_score / game_num
