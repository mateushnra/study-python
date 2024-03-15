from django.shortcuts import render
from .models import Pagamento

from .forms import PagamentoForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request,'index.html')

def pagamento(request):
    pagamentos = Pagamento.objects.order_by('data')
    context = {'pagamentos': pagamentos}
    return render(request,'controle_contas_pagamentos/pagamento.html', context)

def cad_pagamento(request):
    if request.method != 'POST':
        form = PagamentoForm()
    else:
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pagamento'))
    context = {'form':form}
    return render(request,'controle_contas_pagamentos/cad_pagamento.html',context)


def upd_pagamento(request, pk):
    update = Pagamento.objects.get(id=pk)

    if( request.method != "POST"):
        form = PagamentoForm(instance=update)
    else:
        form = PagamentoForm(instance=update, data=request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('pagamento'))
    context = {'update': update, 'pk': pk, 'form': form}
    return render(request, 'controle_contas_pagamentos/upd_pagamento.html', context)

def del_pagamento(request, pk):
    deletar = Pagamento.objects.get(id=pk)
    if(request.method == 'POST'):
        deletar.delete()
        return HttpResponseRedirect(reverse('pagamento'))
    context = {'deletar': deletar, 'pk': pk}
    return render(request, 'controle_contas_pagamentos/del_pagamento.html', context)

        