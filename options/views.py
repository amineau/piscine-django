from django.shortcuts import render
from r00.Data import Data

# Create your views here.
def index(request):
    return render(request, 'options/index.html')

def save_game(request):
    slot = int(request.GET.get('slot', 0))
    data = Data().load()
    save = request.GET.get('save', '')
    if save != '':
        data.save_slot(save)
    context = {
        'slot_current': slot,
        'slot_up': (slot - 1) % 3,
        'slot_down': (slot + 1) % 3,
        'slot_letter': chr(ord('a') + slot)
    }
    return render(request, 'options/save_game.html', context)

def load_game(request):
    return render(request, 'options/load_game.html')
