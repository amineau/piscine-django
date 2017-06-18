from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'options/index.html')

def save_game(request):
    slot = int(request.GET.get('slot', 0))
    context = {
        'slot_current': slot,
        'slot_up': (slot - 1) % 3,
        'slot_down': (slot + 1) % 3,
    }
    return render(request, 'options/save_game.html', context)

def load_game(request):
    return render(request, 'options/load_game.html')
