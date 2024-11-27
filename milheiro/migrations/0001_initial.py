# Generated by Django 5.1.3 on 2024-11-26 20:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Plataforma')),
                ('custo_ponto', models.IntegerField(default=0, verbose_name='Custo por Ponto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarteiraDePontos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontos', models.IntegerField(default=0, verbose_name='Quantidade de Pontos')),
                ('pessoa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='milheiro.pessoa', verbose_name='Dono dos Pontos')),
                ('plataforma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='milheiro.plataforma', verbose_name='Nome da Plataforma')),
            ],
        ),
    ]
