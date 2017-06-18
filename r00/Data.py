import pickle
import random
import os
import shutil
import fnmatch

import sys
from django.conf import settings


class Data:
    singleton = None
    settings = {
        "grid": {'x': 0, 'y': 0},
        "player_position": {'x': 0, 'y': 0},
        "player_movie_balls_count": 10,
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
            if self.get_full_movie(v):
                self.settings['movie_mons'][v] = self.get_full_movie(v)
                self.settings['movie_mons'][v]['id'] = k
                self.settings['movie_mons'][v]['name'] = v
            else:
                print(k, v)
        play_grid = {(0, 0): None}
        for i in range(0, int(settings.GRID['x'])):
            for j in range(0, int(settings.GRID['y'])):
                play_grid[(i, j)] = ({'x': i, 'y': j})
        for i in self.settings['movie_mons']:
            coord = random.choice(play_grid.items())
            play_grid[(coord[1]['x'], coord[1]['y'])]['movie'] = i
        self.settings['max_score'] = len(settings.MOVIES)
        self.settings['play_grid'] = play_grid
        return self.save()

    def save(self):
        pickle.dump(self.settings, open("save.p", "wb"))
        return self.settings

    def save_slot(self, slot):
        try:
            if not os.path.exists('saved_game'):
                os.mkdir('saved_game')
            else:
                for file in os.listdir('saved_game'):
                    if fnmatch.fnmatch(file, 'slot%s*' % (slot)):
                        os.remove(os.path.join('saved_game', file))
        except Exception as e:
            print(e)
            return
        filename = "slot%s_%d_%d.mmg" % (slot, self.get_score(), self.get_max_score())
        try:
            shutil.copyfile("save.p", os.path.join('saved_game', filename))
        except Exception as e:
            print(e)

    def load_slot(self, slot):
        if os.path.exists('saved_game'):
            for file in os.listdir('saved_game'):
                if fnmatch.fnmatch(file, 'slot%s*' % (slot)):
                    try:
                        shutil.copyfile(os.path.join('saved_game', file), "save.p")
                        return True
                    except Exception as e:
                        print(e)
        return False

    def read_save(self):
        result = {}
        if os.path.exists('saved_game'):
            for file in os.listdir('saved_game'):
                infos = file[4:-4].split('_')
                result[infos[0]] = "%s / %s" % (infos[1], infos[2])
        return result

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

    def get_score(self):
        return len(self.settings['movie_dex'])

    def get_max_score(self):
        return len(self.settings['max_score'])

    def get_movie_by_id(self, id):
        return self.settings['movie_mons'][settings.MOVIES[id]]

    def get_movieBalls_count(self):
        return self.settings['player_movie_balls_count']

    def set_movieBall(self, nb):
        self.settings['player_movie_balls_count'] += nb
        self.save()

    def get_moviedex(self):
        return self.settings['movie_dex']

    def set_position(self, pos):
        if pos == "UP" and self.settings['player_position']['x'] > 0:
            self.settings['player_position']['x'] -= 1
        elif pos == "DOWN" and self.settings['player_position']['x'] < self.settings['grid']['x'] - 1:
            self.settings['player_position']['x'] += 1
        elif pos == "LEFT" and self.settings['player_position']['y'] > 0:
            self.settings['player_position']['y'] -= 1
        elif pos == "RIGHT" and self.settings['player_position']['y'] < self.settings['grid']['y'] - 1:
            self.settings['player_position']['y'] += 1
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
            return t
        except KeyError:
            return None

    def remove_from_moviemon(self, key):
        grid = self.settings['play_grid']
        to_del = ()
        for i in grid:
            try:
                if grid[i]['movie'] == key:
                    to_del = i
            except KeyError:
                pass
        self.settings['play_grid'][to_del].pop('movie')
        self.save()

    # change this method for scrapping
    @staticmethod
    def get_full_movie(movie):
        if not movie in settings.FULL_MOVIE:
            return False
        return settings.FULL_MOVIE[movie]
