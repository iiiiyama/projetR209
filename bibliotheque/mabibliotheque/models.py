from django.db import models

# Create your models here.
class Film(models.Model):
    titre = models.CharField(max_length=100)
    réalisateur = models.CharField(max_length=100)
    date_sortie = models.DateField(blank=True, null=True)
    durée = models.IntegerField(blank=False)
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.titre}␣fait␣par␣{self.réalisateur}␣parus␣le␣{self.date_sortie}"
        return chaine