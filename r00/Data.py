import pickle


# Singleton pattern
# http://ogcrazcalm.blogspot.fr/2015/09/singletons-in-python3.html
import io


class Data:
    singleton = None
    settings = {}

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(Data)
        return cls.singleton

    def __init__(self):
        pass

    def __str__(self):
        return str(dict(pickle.load(open("save.p", "rb"))).get("settings"))

    # load settings from backup file
    def load(self):
        self.settings = pickle.load(open("save.p", "rb"))
        return self

    # load settings from settings.py file
    def load_default_settings(self):
        pass

    # save settings to backup file
    def save(self):
        pickle.dump({"settings", self.settings}, open("save.p", "wb"))
        return self

    def dump(self):
        pass

    def get_random_movie(self):
        pass

    def get_strength(self):
        pass

    def get_movie(self):
        pass


def main():
    # initial setup
    d = Data().load_default_settings()
    d.load()

    # d.save()


if __name__ == "__main__":
    main()
