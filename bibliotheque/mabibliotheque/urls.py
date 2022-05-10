from django.urls import path
from . import views
urlpatterns = [
path('index/', views.index),
path('formulaire/', views.formulaire),
path('ajout/', views.ajout),
path('affiche/', views.affiche),
path('affiche/<int:id>/',views.affiche),
path('update/<int:id>/',views.update),
path('updatetraitement/<int:id>/', views.updatetraitement),
path('formulaire2/', views.formulaire2),
path('traitement/', views.traitement),
path('delete/<int:id>/', views.delete),
]
