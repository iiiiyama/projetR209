from django.shortcuts import render

# Create your views here.
from .forms import LivreForm
from . import models

def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            livre = form.save()  # sauvegarde dans la base
            return render(request, "mabibliotheque/affiche.html", {"livre": livre})
        else:
            return render(request, "mabibliotheque/ajout.html", {"form": form})
    else:
        form = LivreForm()
        return render(request, "mabibliotheque/ajout.html", {"form": form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"/bibliotheque/affiche.html",{"livre" : livre})
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})
def affiche(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request, "bibliotheque/affiche.html", {"livre": livre})