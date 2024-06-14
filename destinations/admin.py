from django.contrib import admin

from . import models


class EntidadeAdmin(admin.ModelAdmin):
    ...


class DestinoAdmin(admin.ModelAdmin):
    ...


admin.site.register(models.Entidade, EntidadeAdmin)
admin.site.register(models.Destino, DestinoAdmin)
