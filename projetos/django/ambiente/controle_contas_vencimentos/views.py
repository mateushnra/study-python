from django.shortcuts import render

# Create your views here.

def vencimento(request):
    return render(request,'controle_contas_vencimentos/vencimento.html')