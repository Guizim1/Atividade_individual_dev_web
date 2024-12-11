from django.urls import path
from . import views  # Certifique-se de que views está importado

urlpatterns = [
    path('', views.home, name='home'),  # Exemplo de rota para a página inicial
    path('jogadores/', views.lista_jogadores, name='lista_jogadores'),
    path('jogador/criar/', views.criar_jogador, name='criar_jogador'),
    path('jogador/atualizar/<int:pk>/', views.atualizar_jogador, name='atualizar_jogador'),
    path('jogador/deletar/<int:pk>/', views.deletar_jogador, name='deletar_jogador'),
    path('mestres/', views.lista_mestres, name='lista_mestres'),
    path('mestre/criar/', views.criar_mestre, name='criar_mestre'),
    path('mestre/atualizar/<int:pk>/', views.atualizar_mestre, name='atualizar_mestre'),
    path('mestre/deletar/<int:pk>/', views.deletar_mestre, name='deletar_mestre'),
]
