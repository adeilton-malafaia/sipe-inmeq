from django.urls import path

# from destinations import views
from . import views

urlpatterns = [
    path('entidades/', views.entidades),
    path('entidades-alt/', views.entidades_alt),
    path('destino/', views.destino),
    path('doacao/', views.doacao),
    path('planilha', views.planilha),
]
