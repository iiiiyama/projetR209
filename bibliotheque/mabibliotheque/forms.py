from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class FilmForm(ModelForm):
    class Meta:
        model = models.Film
        fields = ('titre', 'realisateur', 'date_sortie', 'duree','resume', 'acteur',)
        labels = {
            'titre' : _('Titre'),
            'realisateur' : _('Realisateur') ,
            'date_sortie' : _('Date_sortie'),
            'duree' : _('Duree'),
            'resume' : _('Résume'),
            'acteur' : _("Choisissez l'acteur"),
        }

class ActeurForm(ModelForm):
    class Meta:
        model = models.Acteur
        fields = ('nomprenom',)
        labels = {
            'nomprenom' : _('Prenom nom'),
        }