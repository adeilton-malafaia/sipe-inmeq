from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('entidades/', views.entidades),
    path('saidas/', views.saidas),
    path('registrodestino/', views.registrodestino),
    path('planilha', views.planilha),
]
