from django import forms
from django.core.exceptions import ValidationError

from . import models


class EntidadeForm(forms.ModelForm):
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
            "razao": "Razão Social",
            "nf": "Nome de Fantasia",
            "contatos": "Contatos",
            "email": "E-mail",
            "fones": "Telefones",
            "validade": "Validade do cadastro",
            "ativo": "Ativo?",
        }

        help_texts = {}

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
                },  # ignore
            ),
            "nf": forms.TextInput(
                attrs={
                    "required": False,
                }
            ),
            "contatos": forms.TextInput(
                attrs={
                    "required": False,
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "required": False,
                }
            ),
            "fones": forms.TextInput(
                attrs={
                    "required": False,
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
