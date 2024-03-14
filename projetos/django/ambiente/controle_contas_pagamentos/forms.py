from django import forms
from .models import Pagamento

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = "__all__"
        labels = {'descricao': '', 'valor': '','data': '', 'tipo': ''}