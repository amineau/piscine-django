import pickle
import random
import os
import shutil
import fnmatch

from django.conf import settings


class Data:
    singleton = None
    settings = {
        "grid": {'x': 0, 'y': 0},
        "player_position": {'x': 0, 'y': 0},
        "player_movie_balls_count": 0,
        "player_strength": 0,
        "movie_dex": ['Fight_Club','Fight_Club','Fight_Club','Fight_Club','Fight_Club','Fight_Club','Fight_Club','Fight_Club','Fight_Club'],
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
        print(self.settings)
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
                    if fnmatch.fnmatch(file, 'slot%s*'%(slot)):
                        os.remove(os.path.join('saved_game', file))
        except Exception as e:
            print(e)
            return
        filename = "slot%s_%d_%d.mmg"%(slot, self.get_score(), self.get_max_score())
        try:
            shutil.copyfile("save.p", os.path.join('saved_game', filename))
        except Exception as e:
            print(e)

    def load_slot(self, slot):
        if os.path.exists('saved_game'):
            for file in os.listdir('saved_game'):
                if fnmatch.fnmatch(file, 'slot%s*'%(slot)):
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
                result[infos[0]] = "%s / %s"%(infos[1], infos[2])
        return result

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

    def get_score(self):
        return len(self.settings['movie_dex'])

    def get_max_score(self):
        return len(self.settings['movie_mons'])

    def get_moviedex(self):
        return self.settings['movie_dex']

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
