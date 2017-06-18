import pickle
import random

import sys
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
        play_grid = {(0,0): None}
        for i in range (0, int(settings.GRID['x'])):
            for j in range(0, int(settings.GRID['y'])):
                play_grid[(i,j)] = ({'x': i, 'y': j})
        for i in self.settings['movie_mons']:
            coord = random.choice(play_grid.items())
            play_grid[(coord[1]['x'],coord[1]['y'])]['movie'] = i
        self.settings['play_grid'] = play_grid
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

    def add_strenght(self, strenght):
        self.settings["player_strength"] += strenght
        self.save()

    def get_movie(self, key):
        return self.settings['movie_mons'][key]

    def get_movie_by_id(self, id):
        return self.settings['movie_mons'][settings.MOVIES[id]]
    
    def get_movieBalls_count(self):
        return self.settings['player_movie_balls_count']

    def add_movieBall(self):
        self.settings['player_movie_balls_count'] += 1
        self.save()

    def set_position(self, pos):
        print(self.settings['player_position'])
        if pos == "UP" and self.settings['player_position']['x'] > 0:
            self.settings['player_position']['x'] -= 1
        elif pos == "DOWN" and self.settings['player_position']['x'] < self.settings['grid']['x'] - 1:
            self.settings['player_position']['x'] += 1
        elif pos == "LEFT" and self.settings['player_position']['y'] > 0:
            self.settings['player_position']['y'] -= 1
        elif pos == "RIGHT" and self.settings['player_position']['y'] < self.settings['grid']['y'] - 1:
            self.settings['player_position']['y'] += 1
        print(self.settings['player_position'])
        self.save()

    def add_movie_to_movie_dex(self, name):
        self.settings['movie_dex'].append(name)
        self.save()

    def add_movie_to_movie_dex_by_id(self, movie_id):
        self.settings['movie_dex'].append(self.settings['movie_mon'][settings.MOVIES[movie_id]]['name'])
        self.save()

    def is_filled_by_movie(self, req):
        try:
            t = self.settings['movie_mons'][self.settings['play_grid'][(req['x'], req['y'])]['movie']]
            print(t)
            return t
        except KeyError:
            return None

    # change this method for scrapping
    @staticmethod
    def get_full_movie(movie):
        return settings.FULL_MOVIE[movie]
