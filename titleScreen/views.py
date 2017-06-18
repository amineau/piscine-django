from django.shortcuts import render
from r00.Data import Data


# Create your views here.

def index(request):
    data = Data().load()
    print(data)
    return render(request, 'titleScreen/index.html')
