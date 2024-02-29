from django.db import models

ESTADO ={
    ('1','SP'),
    ('2','MG'),
    ('3','RJ'),
}


# Create your models here.
class Address(models.Model):
    
    logradouro = models.CharField(max_length=255,help_text='Digite o endereço')
    numero = models.IntegerField(help_text='Digite o numero do local')
    bairro = models.CharField(max_length=255, help_text='Digite o bairro')
    cidade = models.CharField(max_length=255, null = True, help_text='Digite a Cidade')
    
    
    def __str__(self):
        return self.logradouro
    
    class Meta:
        verbose_name_plural='Endereço'
