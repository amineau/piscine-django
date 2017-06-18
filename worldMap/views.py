from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
    move = request.GET.get('move', '')
    context = {
        'lines': range(settings.GRID[0]),
        'columns': range(settings.GRID[1])
    }
    return render(request, 'worldMap/index.html', context)
