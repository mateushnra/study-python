from django.db import models

# Create your models here.
class Contatos(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False, help_text='nome do contato')
    datanasc = models.DateField(help_text='data de nascimento do contato', verbose_name='Data Nasc.')
    fone = models.IntegerField()
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural ='Contatos'