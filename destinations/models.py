from django.db import models


class Entidade(models.Model):
    cnpj = models.CharField(max_length=14, null=True)  # type: ignore
    razao = models.CharField(max_length=50)  # type: ignore
    nf = models.CharField(max_length=50, null=True, blank=True)  # type: ignore
    contatos = models.CharField(
        max_length=50, null=True, blank=True)  # type: ignore
    email = models.CharField(max_length=50, null=True,
                             blank=True)  # type: ignore
    fones = models.CharField(
        max_length=35, null=True, blank=True)  # type: ignore
    validade = models.DateField()  # type: ignore
    ativo = models.CharField(max_length=1, default="s")  # type: ignore

    def __str__(self):
        return self.razao


class RegistroLancamentos(models.Model):
    dataRegistro = models.DateField()  # type: ignore
    tipoResgistro = models.CharField(max_length=2)
    respINMEQ = models.CharField(max_length=50)  # type: ignore
    testINMEQ = models.CharField(max_length=50)  # type: ignore
    id_entidade = models.ForeignKey(
        Entidade, on_delete=models.SET_NULL, null=True, default=None
    )  # type: ignore

    def __str__(self):
        return str(self.id)


class Lancamento(models.Model):
    data = models.DateField()  # type: ignore
    tc = models.CharField(max_length=7)
    tipo_saida = models.CharField(max_length=2)  # type: ignore
    produto = models.CharField(max_length=60)  # type: ignore
    marca = models.CharField(max_length=50)  # type: ignore
    qn = models.CharField(max_length=10)  # type: ignore
    unid = models.CharField(max_length=5, default=None)  # type: ignore
    quant = models.SmallIntegerField()  # type: ignore
    quant_doado = models.SmallIntegerField()
    quant_inutilizado = models.SmallIntegerField()
    id_registro = models.ForeignKey(
        RegistroLancamentos, on_delete=models.SET_NULL, null=True, default=True
    )

    def __str__(self):
        return str(self.id)
