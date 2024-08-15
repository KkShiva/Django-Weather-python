from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path('weather/', views.weather_view, name='weather'),
    path('Indiaweather/', views.Indiaweather_view, name='Indiaweather'),
    path('USAweather/', views.USAweather_view, name='USAweather'),
    path('Japanweather/', views.Japanweather_view, name='Japanweather'),
    path('Australiaweather/', views.Australiaweather_view, name='Australiaweather'),
    path('Russiaweather/', views.Russiaweather_view, name='Russiaweather'),
    path('SriLankaweather/', views.SriLankaweather_view, name='SriLankaweather'),
    path('Indonesiaweather/', views.Indonesiaweather_view, name='Indonesiaweather'),
]