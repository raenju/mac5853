from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    #path('index/', views.index, name='index')
    path('', views.index, name='index'),
    path('busca/', views.search, name='busca'),
    path('resultado/', views.answer, name='resposta'),
    path('lista/', views.querylist, name='lista')
]