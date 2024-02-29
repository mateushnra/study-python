from django.contrib import admin

from .models import Pagamento
# Register your models here.
class PagamentoAdmin(admin.ModelAdmin):
    list_display=('descricao','valor','data','tipo')

admin.site.register(Pagamento,PagamentoAdmin)
