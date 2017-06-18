from django.shortcuts import render
from r00.Data import Data
import random


# Create your views here.
def index(request, moviemon_id):
    data = Data().load()
    movie = data.get_movie_by_id(int(moviemon_id))
    rate = process_success_rate(data, movie)

    if not request.GET.get("attack", False):
        return render(request, 'battle/index.html',
                      {'Movie': movie, 'strenght': data.get_strength(), 'balls': data.get_movieBalls_count(),
                       'rate': rate, 'info': "{} Appeared ! Try to catch it !".format(movie['name']),
                       'catched': "False"})
    if data.get_movieBalls_count() > 0:
        data.set_movieBall(-1)
    else:
        return render(request, 'battle/index.html',
                      {'Movie': movie, 'strenght': data.get_strength(), 'balls': data.get_movieBalls_count(),
                       'rate': rate, 'info': "Haha You dumbass, you don't have balls", 'catched': "False"})
    random.seed()
    msg = ''
    rdm = random.randint(0, 100)
    catched = "False"
    if rdm < rate:
        data.add_movie_to_movie_dex(movie['name'])
        data.add_strenght(1)
        msg = "Congrat ! you catched {} !He has been added to your Movidex".format(movie['name'])
        catched = "True"
    else:
        msg = "You missed !"
        catched = "False"
    return render(request, 'battle/index.html',
                  {'Movie': movie, 'strenght': data.get_strength(), 'balls': data.get_movieBalls_count(), 'rate': rate,
                   'info': msg, 'catched': catched})


def process_success_rate(data, movie):
    bo = movie['box_office'] / 2
    while (bo > 10):
        bo = bo / 10
    rate = 50 - bo * 10 + data.get_strength() * 5
    rate = max(1, min(rate, 90))
    return rate
