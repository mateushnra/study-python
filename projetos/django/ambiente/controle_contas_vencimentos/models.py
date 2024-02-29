from django.db import models

TIPOPAG=(
    ('1','Dinheiro'),
    ('2','Cartão de Debito'),
    ('3','Cartao de Credito'),
    ('4','PIX'),
    ('5','Boleto'),
)

STATUSPAG=(
    ('1','Pagamento Pendente'),
    ('2','Pagamento parcial'),
    ('3','Pagamento Completo'),
)

# Create your models here.

class Vencimento (models.Model):
    valorTotal = models.DecimalField(max_digits=5,decimal_places=2,null=False,blank=False,help_text='Digite o valor total a pagar')
    dataPagamento = models.DateField(help_text='Informe a data em que foi pago')
    dataVencimento = models.DateField(help_text='Informe a data que venceu o pagamento')
    valorPago  = models.DecimalField(max_digits=5,decimal_places=2, default = 0, help_text = "Informe o valor pago")
    statusPagamento = models.CharField(max_length=15,choices=STATUSPAG, default="1")
    tipo = models.CharField(max_length=15,choices=TIPOPAG,default='4')
    
    def __str__(self):
        return self.dataVencimento