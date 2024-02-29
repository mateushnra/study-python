from django.contrib import admin

from .models import Contatos

class ContatosAdmin(admin.ModelAdmin):
    list_display=('nome','datanasc','fone')

# Register your models here.
admin.site.register(Contatos, ContatosAdmin)
