from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('pesquisa/',views.pesquisa,name='pesquisa'),
    path('orcamentos/',views.orcamentos,name='orcamentos'),
    path('orcamento/<int:orcamento_id>',views.orcamento,name='orcamento')

]