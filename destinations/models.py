# from django.contrib.auth.models import User
from django.db import models


class Entidade(models.Model):
    cnpj = models.IntegerField(primary_key=True)  # type: ignore
    rs = models.CharField(max_length=50)  # type: ignore
    nf = models.CharField(max_length=50, blank=True)  # type: ignore
    contatos = models.CharField(max_length=50, blank=True)  # type: ignore
    email = models.CharField(max_length=50, blank=True)  # type: ignore
    fones = models.CharField(max_length=35, blank=True)  # type: ignore
    validade = models.DateField()  # type: ignore
    ativo = models.CharField(max_length=1)  # type: ignore

    def __str__(self):
        return self.rs


class Lancamento(models.Model):
    id = models.IntegerField(primary_key=True)  # type: ignore
    data = models.DateField()  # type: ignore
    tipo_saida = models.CharField(max_length=2)  # type: ignore
    produto = models.CharField(max_length=60)  # type: ignore
    marca = models.CharField(max_length=50)  # type: ignore
    qn = models.CharField(max_length=10)  # type: ignore
    unid = models.CharField(max_length=5, default=None)  # type: ignore
    quant = models.SmallIntegerField()  # type: ignore
    cnpj = models.ForeignKey(
        Entidade,
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )  # type: ignore

    def __str__(self):
        return self.id


class RegistroLancamentos(models.Model):
    dataRegistro: models.DateField()  # type: ignore
    respINMEQ: models.CharField(max_length=50)  # type: ignore
    testINMEQ: models.CharField(max_length=50)  # type: ignore
