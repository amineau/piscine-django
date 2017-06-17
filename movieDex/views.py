from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'movieDex/index.html')

def detail(request, moviemon_id):
    return render(request, 'movieDex/detail.html', {'moviemon_id': moviemon_id})
