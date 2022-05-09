from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from .forms import FilmForm
from . import models

def ajout(request):
    if request.method == "POST":
        form = FilmForm(request)
        if form.is_valid():
            film = form.save()
            return render(request, "mabibliotheque/affiche.html", {"film": film})
        else:
            return render(request, "mabibliotheque/ajout.html", {"form": form})
    else:
        form = FilmForm()
        return render(request, "mabibliotheque/ajout.html", {"form": form})

def traitement(request):
    lform = FilmForm(request.POST)
    if lform.is_valid():
        film = lform.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request,"mabibliotheque/ajout.html", {"form": lform})

def index(request):
    liste = list(models.Film.objects.all())
    return render(request,"mabibliotheque/index.html",{"liste": liste})

def affiche(request, id):
    film = models.Film.objects.get(pk=id)
    return render(request, "mabibliotheque/affiche.html", {"film": film})

def formulaire(request):
    film = models.Film.objects.get(pk=id)
    return render(request, "mabibliotheque/formulaire.html", {"film": film})

def update(request, id):
    film = models.Film.objects.get(pk=id)
    form = FilmForm(film.repertoire())
    return render(request, "mabibliotheque/ajout.html",{"form":form, "id":id})

def updatetraitement(request, id):
    lform = FilmForm(request.POST)
    if lform.is_valid():
        film = lform.save(commit=False)
        film.id = id
        film.save()
        return HttpResponseRedirect("/mabibliotheque/")
    else:
        return render(request, "mabibliotheque/ajout.html", {"form": lform, "id": id})

def affiche(request, id):
    film = models.Film.objects.get(pk=id)
    return render(request,"bibliotheque/affiche.html",{"film": film})

def formulaireV2(request):
    if request.method == "POST":
        form = FilmForm(request)
        if form.is_valid():
            acteur = form.save()
            return render(request, "mabibliotheque/affiche.html", {"acteur": acteur})
        else:
            return render(request, "mabibliotheque/ajout.html", {"form": form})
    else:
        form = FilmForm()
        return render(request, "mabibliotheque/ajout.html", {"form": form})