from django.contrib import admin

from.models import Address

class AddressAdmin(admin.ModelAdmin):
    list_display=('logradouro','numero','bairro','cidade')
# Register your models here.
admin.site.register(Address, AddressAdmin)