from django.shortcuts import render
from django.conf import settings
from r00.Data import Data

# Create your views here.
def index(request):
    move = request.GET.get('move', '')
    new = request.GET.get('new', '')
    data = Data().load()
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
    print()
    return render(request, 'worldMap/index.html', context)
