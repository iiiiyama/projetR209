from django.db import models

# Create your models here.
class Film(models.Model):
    titre = models.CharField(max_length=100)
    realisateur = models.CharField(max_length=100)
    date_sortie = models.DateField(blank=True, null=True)
    duree = models.IntegerField(blank=False)
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.titre} fait par {self.realisateur} parus le {self.date_sortie}"
        return chaine

    def repertoire(self):
        return {"titre":self.titre, "realisateur":self.realisateur, "date_sortie":self.date_sortie, "duree":self.duree, "resume":self.resume}

class Acteur(models.Model):
    Nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    Date_de_naissance = models.DateField(blank=True, null=True)
    Filmographie = models.CharField(max_length=50)

    def __str__(self):
        chaine = f"{self.prenom}{self.nom} né le {self.Date_de_naissance}"
        return chaine