# from classes.result import Result - WRONG, so I fixed it
from .result import Result

class Game:

    all = []

    def __init__(self, title):
        self.set_title(title)
    
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if hasattr(self, "_title"):
            print("Cannot change Game Title!")
        elif (type(title) is str) and (0 < len(title)):
            print(f"Creating Game {title}!")
            self._title = title
            self.game_results = []
            self.players_list = []
            Game.all.append(self)
        else:
            print("Title must be a STRING LONGER than 0 characters.")
    
    title = property(get_title, set_title)
    
    def results(self):
        self.game_results = []
        for result in Result.all:
            if result.game == self:
                self.game_results.append(result)
        return self.game_results

    def players(self):        
        self.players_list = []
        self.results()
        for result in self.game_results:
            self.players_list.append(result.player)        
        return self.players_list

    def average_score(self, player):
        self.results()
        avg_score = 0
        game_num = 0
        for result in self.game_results:
            if result.player.username == player.username:
                avg_score += result.score
                game_num += 1
        if game_num != 0:
            return avg_score / game_num

    @classmethod
    def check_title(cls, title):
        for game in cls.all:
            if title == game.title:
                return True
        return False