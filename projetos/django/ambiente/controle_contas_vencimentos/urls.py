from django.urls import path

from . import views

urlpatterns = [
    path('controle_contas_vencimentos/vencimento', views.vencimento),
]