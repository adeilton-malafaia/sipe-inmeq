from django import forms
from django.core.exceptions import ValidationError

from . import models

# Primeiro item do select de Entidades cadastradas
op = models.Entidade()
op.cnpj = 0
op.rs = "SELECIONE A ENTIDADE DESEJADA PARA ATUALIZAR DADOS"

# Demais itens com todas as entidades cadastradas
ops = models.Entidade.objects.filter(ativo="s").order_by("rs")

# Criando o iterável com todos os itens
options = [(op.cnpj, op.rs)]
try:
    for item in ops:
        options.append((item.cnpj, item.rs))
except Exception:
    options = options


class EntidadeForm(forms.ModelForm):
    cnpj = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Digite apenas valores numéricos"}
        ),
        error_messages={"required": "Este campo não pode ficar vazio"},
    )

    class Meta:
        model = models.Entidade
        fields = [  # type: ignore
            "cnpj",
            "rs",
            "nf",
            "contatos",
            "email",
            "fones",
            "validade",
            "ativo",
        ]

        labels = {
            "rs": "Razão Social",
            "nf": "Nome de Fantasia",
            "email": "E-mail",
            "fones": "Telefones",
            "validade": "Validade do cadastro",
            "ativo": "Ativo?",
        }

        help_texts = {
            "rs": "A razão social é obrigatória",
            "ativo": "Você deve selecionar uma opção",
            "validade": "A data de validade é obrigatória",
        }

        error_messages = {
            "cnpj": {
                "required": "Este campo não pode ficar vazio",
                "invalid": "Digite apenas números",
            },
            # "rs": {"required": "A razão social não pode ficar vazia"},
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

    select_entidade = forms.ChoiceField(
        choices=(options),
        label="Entidades cadastradas:",
    )

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

    def clean_rs(self):
        data = self.cleaned_data.get("rs")

        if len(data) < 10:
            raise ValidationError(
                [
                    ValidationError(
                        "Este campo não deve ser nulo", code="minlenght"
                    ),  # ignore
                    ValidationError(
                        "Este campo deve ter pelo menos 10 caracteres",
                        code="minlength",  # ignore
                    ),
                ]
            )
