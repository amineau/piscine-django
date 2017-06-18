from django.shortcuts import render
from r00.Data import Data
import random

# Create your views here.
def index(request, moviemon_id):
    data = Data().load()
    movie=data.get_movie_by_id(int(moviemon_id))
    return render(request, 'battle/index.html', {'Movie': movie,'strenght':data.get_strength(),'balls':data.get_movieBalls_count(),'rate':process_success_rate(data, movie)})

def process_success_rate(data, movie):
    bo = movie['box_office'] / 2
    while(bo > 10):
        bo = bo / 10
    rate = 50 - bo * 10 + data.get_strength() * 5
    print(rate)
    rate = max(1, min(rate, 90))
    return rate
