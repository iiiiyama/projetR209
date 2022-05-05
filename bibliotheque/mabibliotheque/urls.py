from django.urls import path
from . import views
urlpatterns = [
path('index/', views.index),
path('formulaire/', views.formulaire),
path('ajout/', views.ajout),
path('affiche/', views.traitement),
path('/update/<int:id>/',views.update),
]
