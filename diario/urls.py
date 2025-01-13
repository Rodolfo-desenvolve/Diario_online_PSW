from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('escrever/', views.escrever, name='escrever'),
    path('cadastra_pessoa/', views.cadastra_pessoa, name='cadastra_pessoa'),
    path('dia/', views.dia, name='dia'),
    path('excluir_dia/', views.excluir_dia, name='excluir_dia')
]