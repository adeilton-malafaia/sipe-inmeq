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
            'validade': 'Validade do cadastro',
            'ativo': 'Ativo?'
        }

        help_texts = {
            'rs': 'A razão social é obrigatória',
            'ativo': 'Você deve selecionar uma opção'
        }

        error_messages = {
            'cnpj': {
                'required': 'Este campo não pode ficar vazio',
                'invalid': 'Digite apenas números'
            }
        }

        widgets = {
            'cnpj': forms.TextInput(),
            'ativo': forms.RadioSelect(
                choices=[('s', 'Sim'), ('n', 'Não')],
                attrs={
                    'class': 'div-row-left',
                }
            ),
            'validade': forms.DateInput(attrs={'type': 'date'})
        }

    select_entidade = forms.ChoiceField(
        choices=(options),
        label='Entidades cadastradas:',
    )
