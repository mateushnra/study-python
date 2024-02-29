from django.shortcuts import render
from .models import Pagamento

# Create your views here.
def index(request):
    return render(request,'index.html')

def pagamento(request):
    pagamentos = Pagamento.objects.order_by('data')
    context = {'pagamentos': pagamentos}
    return render(request,'controle_contas_pagamentos/pagamento.html', context)