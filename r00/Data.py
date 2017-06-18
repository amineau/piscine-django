import pickle
import random

from django.conf import settings


class Data:
    singleton = None
    settings = {
        "grid": [0, 0],
        "player_position": [0, 0],
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
