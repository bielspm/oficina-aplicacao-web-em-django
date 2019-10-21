from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('pesquisa/',views.pesquisa,name='pesquisa'),
    path('orcamentos/',views.orcamentos,name='orcamentos'),
    path('orcamento/<int:orcamento_id>',views.orcamento,name='orcamento'),
    path('edit_orcamento/<int:orcamento_id>',views.edit_orcamento,name='edit_orcamento'),
    path('excluir_orcamento/<int:orcamento_id>',views.excluir_orcamento,name='excluir_orcamento')


]