from django import forms

from . import models

# Primeiro item do select de Entidades cadastradas
op = models.Entidade()
op.cnpj = 0
op.rs = 'SELECIONE A ENTIDADE DESEJADA PARA ATUALIZAR DADOS'

# Demais itens com todas as entidades cadastradas
ops = models.Entidade.objects.filter(ativo='s').order_by('rs')

# Criando o iterável com todos os itens
options = [(op.cnpj, op.rs)]
try:
    for item in ops:
        options.append((item.cnpj, item.rs))
except Exception:
    options = options


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
            'ativo': 'Ativo?'
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
        choices=(options),
        label='Entidades cadastradas:',
    )
