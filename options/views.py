from django.shortcuts import render
from r00.Data import Data

# Create your views here.
def index(request):
    return render(request, 'options/index.html')

def get_context(slot):
    data = Data().load()
    saved_res = data.read_save()
    saved = {}
    for c in "abc":
        if c in saved_res:
            saved[c] = saved_res[c]
        else:
            saved[c] = "Free"
    return {
        'slot_current': slot,
        'slot_up': chr((ord(slot) - 98) % 3 + 97),
        'slot_down': chr((ord(slot) - 96) % 3 + 97),
        'saved': saved,
    }

def save_game(request):
    slot = request.GET.get('slot', 'a')
    toSave = request.GET.get('save', '')
    if toSave != '':
        Data().load().save_slot(toSave)
    context = get_context(slot)
    return render(request, 'options/save_game.html', context)

def load_game(request):
    slot = request.GET.get('slot', 'a')
    context = get_context(slot)
    return render(request, 'options/load_game.html', context)
