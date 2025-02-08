from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('local/', views.local, name='local'),
    path('exibiritem/<int:id>/', views.exibiritem, name='exibiritem'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    path('dia/<int:num>/', views.dia_da_semana, name='dia_da_semana'),
    path('dados/', views.dados, name='dados'),
    path('form/', views.form, name='form'),
    path('alunos/listar/', views.listar_aluno, name='listar_aluno'),
]