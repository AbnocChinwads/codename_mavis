from django.shortcuts import render

# Create your views here.
def game(request):
    """ A view to return the index page """
    return render(request, 'game/game.html')
