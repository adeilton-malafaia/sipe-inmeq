from django import forms
from django.core.exceptions import ValidationError

from . import models


class EntidadeForm(forms.ModelForm):
    class Meta:
        model = models.Entidade
        fields = [
            "cnpj",
            "razaosocial",
            "nf",
            "contatos",
            "email",
            "fones",
            "validade",
            "ativo",
        ]

        labels = {
            "razaosocial": "Razão Social",
            "nf": "Nome de Fantasia",
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
        }

        widgets = {
            "cnpj": forms.TextInput(
                attrs={
                    "placeholder": "Digite apenas números",
                },
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
        data = self.cleaned_data.get("cnpj")

        if len(str(data)) < 14:
            raise ValidationError(
                [
                    ValidationError(
                        "Este campo não deve ser nulo",
                        code="minlenght",
                    ),
                    ValidationError(
                        "Este campo não deve ter menos de 14 dígitos",
                        code="minlenght",
                    ),
                ]
            )

    def clean_razaosocial(self):
        data = self.cleaned_data.get("razaosocial")

        if len(data) < 10:
            raise ValidationError(
                [
                    ValidationError("Este campo não deve ser nulo", code="invalid"),
                    ValidationError(
                        "Este campo deve ter pelo menos 10 caracteres",
                        code="minlength",
                    ),
                ]
            )
        else:
            self.cleaned_data["razaosocial"] = data
