# from django.contrib.auth.models import User
from django.db import models


class Entidade(models.Model):
    cnpj = models.IntegerField(
        primary_key=True,
        blank=True,
        help_text="Este campo não pode ficar vazio",
        # error_messages={
        #     'required': 'O CNPJ não pode ficar vazio',
        #     'invalid': 'CNPJ só pode ter números'
        # }
    )  # type: ignore
    rs = models.CharField(max_length=50, blank=True)
    nf = models.CharField(max_length=50, blank=True)
    contatos = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    fones = models.CharField(max_length=35, blank=True)
    validade = models.DateField()
    ativo = models.CharField(max_length=1)

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
        Entidade, on_delete=models.SET_NULL, null=True, default=None
    )  # type: ignore

    def __str__(self):
        return self.id


class RegistroLancamentos(models.Model):
    dataRegistro: models.DateField()  # type: ignore
    respINMEQ: models.CharField(max_length=50)  # type: ignore
    testINMEQ: models.CharField(max_length=50)  # type: ignore
