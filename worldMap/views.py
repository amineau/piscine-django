from django.shortcuts import render
from django.conf import settings
from r00.Data import Data

# Create your views here.
def index(request):
    data = Data().load()
    move = request.GET.get('move', '')
    new = request.GET.get('new', '')
    if new == 'true':
        data.load_default_settings()
    # print(data)
    context = {
        'lines': range(data['grid'][0]),
        'columns': range(data['grid'][1])
    }
    return render(request, 'worldMap/index.html', context)
