from django.shortcuts import render
from r00.Data import Data

# Create your views here.

def index(request):
    # change the position of this line to be started at server startup
    d = Data().load_default_settings()
    print(d)
    # we need to use d = Data().load() instead of
    return render(request, 'titleScreen/index.html')
