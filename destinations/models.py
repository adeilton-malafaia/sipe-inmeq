from django.db import models


class Entidade(models.Model):
    cnpj = models.CharField(max_length=14, null=True)
    razao = models.CharField(max_length=50)
    nf = models.CharField(max_length=50, null=True, blank=True)
    contatos = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50)
    fones = models.CharField(max_length=35, default="Sem fones")
    validade = models.DateField()
    ativo = models.CharField(max_length=1, default="s")

    def __str__(self):
        return self.razao


class Lancamento(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.DateField()
    tipo_saida = models.CharField(max_length=2)
    produto = models.CharField(max_length=60)
    marca = models.CharField(max_length=50)
    qn = models.CharField(max_length=10)
    unid = models.CharField(max_length=5, default=None)
    quant = models.SmallIntegerField()
    cnpj = models.ForeignKey(
        Entidade, on_delete=models.SET_NULL, null=True, default=None
    )

    def __str__(self):
        return str(self.id)


class RegistroLancamentos(models.Model):
    dataRegistro: models.DateField()  # type: ignore
    respINMEQ: models.CharField(max_length=50)  # type: ignore
    testINMEQ: models.CharField(max_length=50)  # type: ignore
