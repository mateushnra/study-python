from django.db import models
TIPOPAG=(
    ('1','Dinheiro'),
    ('2','Cartão de Debito'),
    ('3','Cartao de Credito'),
    ('4','PIX'),
    ('5','Boleto'),
)

# Create your models here.
class Pagamento(models.Model):
    descricao= models.CharField(max_length=255,null=False,blank=False,help_text='Descreva o seu pagamento')
    valor=models.DecimalField(max_digits=5,decimal_places=2,null=False,blank=False,help_text='Digite o valor do pagamento')
    data = models.DateField(help_text='Informe quando sera o pagamento')
    tipo = models.CharField(max_length=15,choices=TIPOPAG,default='4')
    
    def __str__(self):
        return self.descricao