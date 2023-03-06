from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.index, {'name': 'Home'}, name='home'),
    path('restaurant/', views.index, {'name': 'About the restaurant'}, name='restaurant'),
    path('pizza/', views.index, {'name': 'Pizza'}, name='pizza'),
    path('pizza/hawaii', views.index, {'name': 'Pizza Hawaii'}, name='pizza_hawaii'),
    path('pizza/hawaii/big', views.index, {'name': 'Pizza Hawaii/Big'}, name='pizza_hawaii_big'),
    path('pizza/hawaii/regular', views.index, {'name': 'Pizza Hawaii/Regular'}, name='pizza_hawaii_regular'),
    path('pizza/4seasons', views.index, {'name': 'Pizza Four Seasons'}, name='pizza_4seasons'),
    path('pizza/4seasons/big', views.index, {'name': 'Pizza Four Seasons/Big'}, name='pizza_4seasons_big'),
    path('pizza/4seasons/regular', views.index, {'name': 'Pizza Four Seasons/Regular'}, name='pizza_4seasons_regular'),
    path('drink/', views.index, {'name': 'Drink'}, name='drink'),
    path('drink/soft_drink', views.index, {'name': 'Drink Soft Drink'}, name='drink_soft'),
    path('drink/water', views.index, {'name': 'Drink water'}, name='drink_water'),
]

