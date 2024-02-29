from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('controle_contas_pagamentos/pagamento', views.pagamento, name='pagamento'),
]