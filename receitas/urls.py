from django.urls import path
from . import views # aqui ele está importando do próprio módulo(.) do diretório

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar')
]