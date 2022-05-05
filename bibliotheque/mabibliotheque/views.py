from django.shortcuts import render

# Create your views here.
from .forms import FilmForm
from . import models

def index(request):
    return render(request, 'mabibliotheque/index.html')

def ajout(request):
    if request.method == "POST":
        form = FilmForm(request)
        if form.is_valid():
            livre = form.save()  # sauvegarde dans la base
            return render(request, "mabibliotheque/affiche.html", {"livre": livre})
        else:
            return render(request, "mabibliotheque/ajout.html", {"form": form})
    else:
        form = FilmForm()
        return render(request, "mabibliotheque/ajout.html", {"form": form})

def traitement(request):
    lform = FilmForm(request.POST)
    if lform.is_valid():
        film = lform.save()
        return render(request,"/bibliotheque/affiche.html",{"film" : film})
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})
def affiche(request, id):
    film = models.Film.objects.get(pk=id)
    return render(request, "bibliotheque/affiche.html", {"film": film})
def formulaire(request):
    film = models.Film.objects.get(pk=id)
    return render(request, "bibliotheque/formulaire.html", {"film": film})