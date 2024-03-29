# Generated by Django 5.0.2 on 2024-02-22 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(help_text='Descreva o seu pagamento', max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, help_text='Digite o valor do pagamento', max_digits=5)),
                ('data', models.DateField(help_text='Imforme quando sera o pagamento')),
                ('tipo', models.CharField(choices=[('1', 'Dinheiro'), ('2', 'Cartão de Debito'), ('3', 'Cartao de Credito'), ('4', 'PIX'), ('5', 'Boleto')], default='4', max_length=15)),
            ],
        ),
    ]
