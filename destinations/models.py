from django.db import models


class Entidade(models.Model):
    cnpj = models.CharField(max_length = 18)
    rs = models.CharField(max_length = 50)
    nf = models.CharField(max_length = 50)
    contatos = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    fones = models.CharField(max_length = 35)
    validade = models.TimeField()
    ativo = models.CharField(max_length = 1)
