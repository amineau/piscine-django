import pickle
import random

from django.conf import settings


class Data:
    singleton = None
    settings = {
        "grid": {'x': 0, 'y': 0},
        "player_position": {'x': 0, 'y': 0},
        "player_movie_balls_count": 0,
        "player_strength": 0,
        "movie_dex": [],
        "movie_mons": {}
    }

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(Data)
        return cls.singleton

    def __init__(self):
        pass

    def __str__(self):
        return str(dict(pickle.load(open("save.p", "rb"))))

    def load(self):
        self.settings = pickle.load(open("save.p", "rb"))
        return self

    def load_default_settings(self):
        self.settings['grid'] = settings.GRID
        self.settings['player_position'] = settings.BEGIN
        # from the list of movies in the settings, load the movies in settings.movie_mons
        movie_list = settings.MOVIES
        for k, v in movie_list.items():
            self.settings['movie_mons'][v] = self.get_full_movie(v)
            self.settings['movie_mons'][v]['id'] = k
            self.settings['movie_mons'][v]['name'] = v
        print(self.settings)
        return self.save()

    def save(self):
        pickle.dump(self.settings, open("save.p", "wb"))
        return self.settings

    def dump(self):
        return self.settings

    def get_random_movie(self):
        movies_outer_join = {k: v for k, v in self.settings['movie_mons'].items() if
                             k not in self.settings['movie_dex']}
        return random.choice(movies_outer_join)

    def get_strength(self):
        return self.settings["player_strength"]

    def get_movie(self, key):
        return self.settings['movie_mons'][key]

    def get_movie_by_id(self, id):
        return self.settings['movie_mons'][settings.MOVIES[id]]

    def set_position(self, pos):
        if pos == "UP" and self.settings['player_position']['y'] > 0:
            self.settings['player_position']['y'] -= 1
        elif pos == "DOWN" and self.settings['player_position']['y'] < self.settings['grid']['y']:
            self.settings['player_position']['y'] += 1
        elif pos == "LEFT" and self.settings['player_position']['x'] > 0:
            self.settings['player_position']['x'] -= 1
        elif pos == "RIGHT" and self.settings['player_position']['x'] < self.settings['grid']['x']:
            self.settings['player_position']['x'] += 1
        else:
            raise Exception("invalid move command")
        self.save()

    # change this method for scrapping
    @staticmethod
    def get_full_movie(movie):
        return settings.FULL_MOVIE[movie]
