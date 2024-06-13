from django.urls import path

# from destinations import views
from . import views

urlpatterns = [
    path('entidades/', views.entidades),
    path('destino/', views.destino),
    path('doacao/', views.doacao),
    path('planilha', views.planilha),
]
