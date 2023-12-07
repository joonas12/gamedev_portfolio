"""Defines URL patterns for travel journals."""
from django.urls import path 
from . import views 

app_name = 'game_portfolio'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page that shows all loactions.
    path('tests', views.tests, name='Tests'),
]