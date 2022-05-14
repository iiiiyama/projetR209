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
path('traitement/', views.traitement),
path('delete/<int:id>/', views.delete),
path('formulaire2/', views.formulaire2),
path('traitement2/', views.traitement2),
path('delete2/<int:id>/', views.delete2),
path('update2/<int:id>/',views.update2),
path('updatetraitement2/<int:id>/', views.updatetraitement2),
path('affiche2/', views.affiche2),
path('affiche2/<int:id>/',views.affiche2),
path('index2/', views.index2),
]