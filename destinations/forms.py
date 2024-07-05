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

        labels = {
            'rs': 'Razão Social',
            'nf': 'Nome de Fantasia',
            'email': 'E-mail',
            'fones': 'Telefones',
        }

        widgets = {
            'cnpj': forms.TextInput(),
            # 'validade': forms.DateTimeField()
            'ativo': forms.RadioSelect(
                choices=[('s', 'Sim'), ('n', 'Não')],
                attrs={
                    'class': 'div-row-left',
                }
            )
        }

    select_entidade = forms.ChoiceField(
        # choices=[models.Entidade.objects.all()],
        label='Entidades cadastradas:'
    )

    select_entidade.label
