from django.urls import path

from . import views

app_name = 'destinations'

urlpatterns = [
    path('', views.home, name='home'),
    path('entidades/', views.entidades, name='entidade'),
    path('saidas/', views.saidas, name='saidas'),
    path('registrodestino/', views.registrodestino, name='registrodestino'),
    path('planilha', views.planilha, name='palnilha'),
]
