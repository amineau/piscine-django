from django.shortcuts import render
from r00.Data import Data

# Create your views here.

def index(request):
    data = Data().load()
    movie_dex = data.get_moviedex()
    move = request.GET.get('move', '')
    selected = int(request.GET.get('selected', 0))
    if move == 'right':
        selected = (selected + 1) % len(movie_dex)
    elif move =='left':
        selected = (selected - 1) % len(movie_dex)
    posters = []
    id = 0
    for movie in movie_dex:
        posters.append({
            'src': data.get_full_movie(movie)['poster'],
            'id': id
        })
        id += 1
    if len(movie_dex) and selected < len(movie_dex):
        select = {
            'id': selected,
            'name': movie_dex[selected],
        }
    else:
        select = False
    context = {
        'posters': posters,
        'select': select,
    }
    return render(request, 'movieDex/index.html', context)

def detail(request, moviemon_id):
    return render(request, 'movieDex/detail.html', {'moviemon_id': moviemon_id})
