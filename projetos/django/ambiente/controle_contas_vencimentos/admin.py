from django.contrib import admin

from .models import Vencimento
# Register your models here.

class VencimentoAdmin(admin.ModelAdmin):
    list_display=('valorTotal','statusPagamento', 'dataVencimento', 'dataPagamento', 'valorPago', 'tipo')

admin.site.register(Vencimento, VencimentoAdmin)