from django import forms
from django.core.exceptions import ValidationError

from . import models


class EntidadeForm(forms.ModelForm):
    option = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = models.Entidade
        fields = [
            "cnpj",
            "razao",
            "nf",
            "contatos",
            "email",
            "fones",
            "validade",
            "ativo",
        ]

        labels = {
            'cnpj': 'cnpj',
            "razao": "Razão Social",
            "nf": "Nome de Fantasia",
            "contatos": "Contatos",
            "email": "E-mail",
            "fones": "Telefones",
            "validade": "Validade do cadastro",
            "ativo": "Ativo?",
        }

        # help_texts = {}

        error_messages = {
            "cnpj": {
                "required": "Este campo não pode ficar vazio",
                "invalid": "Digite apenas números",
            },
            "validade": {"required": "Defina uma data para a validade"},
            "contatos": {"required": "Defina pelo menos um contato"},
            "razão": {"required": "Razão Social não pode ser nulo"},
        }

        widgets = {
            "cnpj": forms.TextInput(
                attrs={
                    "placeholder": "Digite apenas números",
                    "maxlength": 14,
                },
            ),
            "razao": forms.TextInput(
                attrs={
                    'placeholder': 'Digite algo com pelo menos 10 caracteres aqui'
                }
            ),
            "ativo": forms.RadioSelect(
                choices=[("s", "Sim"), ("n", "Não")],
                attrs={
                    "class": "div-row-left",
                },
            ),
            "validade": forms.DateInput(attrs={"type": "date"}),
        }

    # Validações por campo

    def clean_cnpj(self):
        data = self.cleaned_data["cnpj"]

        if len(data) != 14:
            raise ValidationError(
                [
                    ValidationError(
                        "O CNPJ não pode ser nulo", code="invalid"
                    ),  # ignore
                    ValidationError(
                        "O CNPJ deVE ter 14 dígitos", code="invalid"
                    ),  # ignore
                ]
            )

        cnpj_test = models.Entidade.objects.filter(cnpj=data)

        if len(cnpj_test) > 0:
            raise ValidationError(
                "Já existe uma Entidade com este CNPJ",
            )

        return data


class EntidadeUpdateForm(EntidadeForm):
    ents = models.Entidade.objects.filter(ativo='s')
    opt = [('0', 'SELECIONE UMA ENTIDADE PARA ATUALIZAR')]
    for item in ents:
        opt.append((item.cnpj, item.razao))
    cnpj = forms.CharField(widget=forms.Select(choices=opt))
