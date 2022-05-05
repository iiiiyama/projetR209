from django.db import models

# Create your models here.
class Film(models.Model):
    titre = models.CharField(max_length=100)
    realisateur = models.CharField(max_length=100)
    date_sortie = models.DateField(blank=True, null=True)
    duree = models.IntegerField(blank=False)
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.titre}␣fait␣par␣{self.realisateur}␣parus␣le␣{self.date_sortie}"
        return chaine

    def repertoire(self):
        return {"titre":self.titre, "realisateur":self.realisateur, "date_sortie":self.date_sortie, "duree":self.duree, "resume":self.resume}