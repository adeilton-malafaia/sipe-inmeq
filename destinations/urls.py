from django.urls import path

from . import views

app_name = 'destinations'

urlpatterns = [
    path('', views.home, name='home'),
    path('entidades/cadastro/', views.entidades_insert, name='entidade-insert'),  # noqa: E501
    path('entidades/atualizar/', views.entidades_update,
         name='entidade-update'),  # ignore
    path('saidas/', views.saidas, name='saidas'),
    path('entidades/registrodestino/', views.registrodestino, name='entidade-registrodestino'),  # noqa: E501
    path('planilha/', views.planilha, name='entidades-planilha'),
]
