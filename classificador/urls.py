from django.conf.urls import url
from django.urls import path
from django.http import HttpResponseRedirect

from . import views

urlpatterns = [
    path('', lambda r: HttpResponseRedirect('index/')),
    path('index/', views.index, name='index'),
    path('busca/', views.search, name='busca'),
    path('resultado/', views.answer, name='resposta'),
    path('lista/', views.querylist, name='lista'),

    path('urls_submit/', views.urls_submit, name='urls_submit'),
    path('search_submit/', views.search_submit, name='search_submit')
]