# Generated by Django 5.0.2 on 2024-02-15 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(help_text='Digite o endereço', max_length=255)),
                ('numero', models.IntegerField(help_text='Digite o numero do local')),
                ('bairro', models.CharField(help_text='Digite o bairro', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Endereço',
            },
        ),
    ]
