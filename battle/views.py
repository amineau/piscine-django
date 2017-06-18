from django.shortcuts import render
from r00.Data import Data

# Create your views here.
def index(request, moviemon_id):
    data = Data().load()
    print(data.get_movie_by_id(int(moviemon_id)))
    return render(request, 'battle/index.html', {'moviemon_id': moviemon_id})
