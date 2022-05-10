from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class FilmForm(ModelForm):
    class Meta:
        model = models.Film
        fields = ('titre', 'realisateur', 'date_sortie', 'duree','resume')
        labels = {
            'titre' : _('Titre'),
            'realisateur' : _('Realisateur') ,
            'date_sortie' : _('Date_sortie'),
            'duree' : _('Duree'),
            'resume' : _('Résume')
        }

class ActeurForm(ModelForm):
    class Meta:
        model = models.Acteur
        fields = ('nom', 'prenom', 'date_de_naissance', 'filmographie')
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prenom') ,
            'date_de_naissance' : _('Date_de_naissance'),
            'filmographie' : _('Filmographie'),
        }