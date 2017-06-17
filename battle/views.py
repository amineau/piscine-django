from django.shortcuts import render

# Create your views here.
def index(request, moviemon_id):
    return render(request, 'battle/index.html', {'moviemon_id': moviemon_id})
