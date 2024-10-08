from django import forms
from django.core.exceptions import ValidationError

from destinations.models import Entidade


class EntidadeForm(forms.ModelForm):
    option = forms.CharField(widget=forms.HiddenInput())
    selectEntidade = forms.CharField(
        label='Entidade',
        widget=forms.Select()
    )

    class Meta:
        model = Entidade
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
                    'placeholder': 'Digite algo com pelo menos 10 caracteres aqui'  # noqa: E501
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
        nao_numerico = None
        try:
            int(data)
            nao_numerico = False
        except Exception:
            nao_numerico = True

        if nao_numerico:
            raise ValidationError(
                "Digite apenas números",
                code='invalid'
            )

        if len(data) < 14 or nao_numerico:
            raise ValidationError(
                [
                    ValidationError(
                        "O CNPJ não pode ser nulo", code="invalid"
                    ),  # ignore
                    ValidationError(
                        "O CNPJ deve ter 14 dígitos", code="invalid"
                    ),  # ignore
                    ValidationError(
                        'Digite apenas números',
                        code='invalid'
                    )
                ]
            )

        return data

    def clean_razao(self):
        data = self.cleaned_data['razao']

        if len(data) < 10:
            raise ValidationError(
                'Digite algo com pelo menos 10 caracteres',
                code='invalid'
            )

        return data


class CronogramaForm(forms.Form):
    crono = forms.FileField(
        widget=forms.FileInput(attrs={'accept': '.pdf'})
    )

    option = forms.CharField(
        widget=forms.HiddenInput()
    )

    data = forms.DateField()
    tc = forms.CharField()
    produto = forms.CharField()
    marca = forms.CharField()
    qn = forms.CharField()
    quant = forms.CharField()
    opt = [
        ('dt', 'Doação total'),
        ('dp', "Doação parcial"),
        ('rt', 'Retirada'),
        ('in', 'Inutilização')
    ]
    tipo_saida = forms.CharField(
        widget=forms.Select(choices=opt)
    )
