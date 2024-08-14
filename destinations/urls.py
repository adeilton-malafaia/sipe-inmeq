from django.urls import path

from . import views

app_name = 'destinations'

urlpatterns = [
    path('', views.home, name='home'),
    path('entidades/cadastro/', views.entidades_insert, name='entidade-insert'),  # noqa: E501
    path('entidades/atualizar/', views.entidades_update,
         name='entidade-update'),  # ignore
    path('saidas/', views.saidas, name='saidas'),
    path('saidas/load', views.loadCronograma, name='load-saidas'),
    path('saidas/registrodestino/', views.registrodestino, name='registrodestino'),  # noqa: E501
    path('planilha/', views.planilha, name='planilha'),
]
