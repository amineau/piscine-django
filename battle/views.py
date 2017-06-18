from django.shortcuts import render
from r00.Data import Data

# Create your views here.
def index(request, moviemon_id):
    data = Data().load()
    movie=data.get_movie_by_id(int(moviemon_id))
    return render(request, 'battle/index.html', {'Movie': movie})
