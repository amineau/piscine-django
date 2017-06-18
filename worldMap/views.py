from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse

from r00.Data import Data

# Create your views here.
def index(request):
    move = request.GET.get('move', '')
    new = request.GET.get('new', '')
    data = Data().load()
    if move:
        data.set_position(move.upper())
    if new == 'true':
        data.load_default_settings()
    settings = data.dump()
    context = {
        'grid': {
            'x': range(settings['grid']['x']),
            'y': range(settings['grid']['y']),
        },
        'player_position': settings['player_position'],
        'movieballs': settings['player_movie_balls_count'],
    }
    movie_present = data.is_filled_by_movie(settings['player_position'])
    if movie_present is None:
        return render(request, 'worldMap/index.html', context)
    else:
        return redirect('/battle/' + str(movie_present['id']))
