from django.contrib.auth.models import User
from django.db import models
from django.db.models import F
from django.db.models.functions import datetime


# Create your models here.


class Plataforma(models.Model):
    nome = models.CharField(verbose_name="Nome da Plataforma", max_length=100)
    custo_ponto = models.FloatField(verbose_name="Custo por Ponto", default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"


class CarteiraDePontos(models.Model):
    plataforma = models.ForeignKey(Plataforma, verbose_name="Nome da Plataforma", null=True, on_delete=models.SET_NULL)
    pessoa = models.ForeignKey(User, verbose_name="Dono dos Pontos", null=True, on_delete=models.SET_NULL)
    pontos = models.IntegerField(verbose_name="Quantidade de Pontos", default=0)
    valor = models.FloatField(verbose_name="Valor", default=0)
    custo_milheiro = models.GeneratedField(
        expression=((F("valor") * 1000) / F("pontos")),
        output_field=models.FloatField(),
        db_persist=True,
    )
    descricao = models.CharField(verbose_name="Descrição", max_length=200)
    data_aquisicao = models.DateField(verbose_name="Data de Aquisição")
    data_expiracao = models.DateField(verbose_name="Data de Expiração")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Carteira de Pontos"

    def __str__(self):
        return f"{self.plataforma} - {self.pontos}"

