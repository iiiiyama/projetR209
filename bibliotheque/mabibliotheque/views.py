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
        return HttpResponseRedirect("/mabibliotheque/index/")
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
        return HttpResponseRedirect("/mabibliotheque/index/")
    else:
        return render(request, "mabibliotheque/ajout.html", {"form": lform, "id": id})

def delete(request, id):
    film = models.Film.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/mabibliotheque/index/")

######################## second formulaire #####################################

def formulaire2(request):
    if request.method == "POST":
        form = ActeurForm(request)
        if form.is_valid():
            Acteur = form.save()
            return render(request, "mabibliotheque/affiche.html", {"acteur": Acteur})
        else:
            return render(request, "mabibliotheque/formulaire2.html", {"form": form})
    else:
        form = FilmForm()
        return render(request, "mabibliotheque/formulaire2.html", {"form": form})

def delete(request, id):
    film = models.Film.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/mabibliotheque/index/")