from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'options/index.html')

def save_game(request):
    return render(request, 'options/save_game.html')

def load_game(request):
    return render(request, 'options/load_game.html')
