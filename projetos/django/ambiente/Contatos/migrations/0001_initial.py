# Generated by Django 5.0.2 on 2024-02-09 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='nome do contato', max_length=200)),
                ('datanasc', models.DateField(help_text='data de nascimento do contato')),
                ('fone', models.IntegerField()),
            ],
        ),
    ]