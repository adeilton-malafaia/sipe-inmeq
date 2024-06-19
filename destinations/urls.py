from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('entidades/', views.entidades),
    path('destino/', views.destino),
    path('doacao/', views.doacao),
    path('planilha', views.planilha),
]
