from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.get_users, name='get_all_users'),
    path('scripts', views.listar_scripts, name='listar_todos_scripts'),
    path('cadastrar-script', views.cadastrar_script, name='cadastrar_script'),
    path('editar-script/<int:id>', views.editar_script, name='editar_script'),
    path('excluir-script/<int:id>', views.excluir_script, name='excluir_script'),

    path('pessoas', views.listar_pessoas, name='listar_pessoas'),
    path('cadastrar-pessoa', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('editar-pessoa/<int:id>', views.editar_pessoa, name='editar_pessoa'),
    path('excluir-pessoa/<int:id>', views.excluir_pessoa, name='excluir_pessoa'),
    path('pessoas-por-ids', views.listar_pessoas_por_ids, name='listar_pessoas_por_ids'),
    path('pessoas-por-nome', views.listar_pessoas_por_nome, name='listar_pessoas_por_nome'),

    path('indicadores', views.listar_indicadores, name='listar_indicadores'),
    path('cadastrar-indicador', views.cadastrar_indicador, name='cadastrar_indicador'),
    path('editar-indicador/<int:id>', views.editar_indicador, name='editar_indicador'),
    path('excluir-indicador/<int:id>', views.excluir_indicador, name='excluir_indicador'),
    path('indicadores-por-nome', views.listar_indicadores_por_nome, name='listar_indicadores_por_nome'),

    path('visualizar-setores/', views.visualizar_setores, name='visualizar-setores'),
    path('cadastrar-setores', views.cadastrar_setores, name='cadastrar-setores'),
    path('editar-setores/<int:id>', views.editar_setores, name='editar-setores'),
    path('excluir-setores/<int:id>', views.excluir_setores, name='excluir-setores'),


    path('redefinir-senha', views.redefinir_senha, name='redefinir_senha'),
    path('alterar-senha', views.alterar_senha, name='alterar_senha'),








    # path('inicio', views.listar_informacoes_inicio, name='listar_informacoes_inicio'),


    # path('relatorio', views.gerar_relatorio, name='gerar-relatorio')

]
