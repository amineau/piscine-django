import pickle
from django.conf import settings


class Data:
    singleton = None
    settings = {}

    # the constructor follows the singleton pattern
    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(Data)
        return cls.singleton

    def __init__(self):
        pass

    def __str__(self):
        return str(dict(pickle.load(open("save.p", "rb"))))

    # load settings from backup file
    def load(self):
        self.settings = pickle.load(open("save.p", "rb"))
        return self

    # load settings from settings.py file (put the data of the settings file here)
    # after loading data, the settings are saved in the backup file
    def load_default_settings(self):
        self.settings['grid'] = settings.GRID
        return self.save()

    # save settings to backup file
    def save(self):
        pickle.dump(self.settings, open("save.p", "wb"))
        return self.settings

    def dump(self):
        return self.settings

    def get_random_movie(self):
        pass

    def get_strength(self):
        pass

    def get_movie(self):
        pass
