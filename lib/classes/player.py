from classes.result import Result

class Player:

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
            Player.add_to_player_list(self)
    
    username = property(get_username, set_username)

    @classmethod
    def add_to_player_list(cls, self):
        cls.all.append(self)
        print(cls.all)

        

    def results(self):
        # TODO: Implement this method
        pass

    def games_played(self):
        # TODO: Implement this method
        pass

    def played_game(self, game):
        # TODO: Implement this method
        pass

    def num_times_played(self, game):
        # TODO: Implement this method
        pass

    def add_result(self, game, score):
        # TODO: Implement this method
        pass