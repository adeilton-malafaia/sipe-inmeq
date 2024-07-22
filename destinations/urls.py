from django.urls import path

from . import views

app_name = 'destinations'

urlpatterns = [
    path('', views.home, name='home'),
    path('entidades/cadastro', views.entidades_insert, name='entidade-insert'),
    path('entidades/atualizar', views.entidades_update,
         name='entidade-update'),  # ignore
    path('saidas/', views.saidas, name='saidas'),
    path('registrodestino/', views.registrodestino, name='registrodestino'),
    path('planilha', views.planilha, name='palnilha'),
]
