from django import forms

from . import models


class EntidadeForm(forms.ModelForm):
    class Meta:
        model = models.Entidade
        fields = [  # type: ignore
            'cnpj',
            'rs',
            'nf',
            'contatos',
            'email',
            'fones',
            'validade',
            'ativo',
        ]
