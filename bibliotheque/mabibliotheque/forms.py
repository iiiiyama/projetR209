from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class FilmForm(ModelForm):
    class Meta:
        model = models.Film
        fields = ('titre', 'réalisateur', 'date_sortie', 'durée','resume')
        labels = {
            'titre' : _('Titre'),
            'réalisateur' : _('Réalisateur') ,
            'date_sortie' : _('Date_sortie'),
            'durée' : _('Durée'),
            'resume' : _('Résumé')
        }