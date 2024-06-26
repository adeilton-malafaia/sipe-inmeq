from django.contrib import admin

from . import models


@admin.register(models.Entidade)
class EntidadeAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    ...
