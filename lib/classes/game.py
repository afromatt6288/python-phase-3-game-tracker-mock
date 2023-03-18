from classes.result import Result

class Game:

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
            Game.add_to_game_list(self)
    
    title = property(get_title, set_title)

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
