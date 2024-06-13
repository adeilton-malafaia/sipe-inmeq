from django.urls import path

from destinations.views import destino, doacao, entidades, planilha

urlpatterns = [
    path('entidades/', entidades),
    path('destino/', destino),
    path('doacao/', doacao),
    path('planilha', planilha),
]
