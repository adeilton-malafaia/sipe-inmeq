from unittest import skip

from django.test import TestCase
from parameterized import parameterized

from destinations.forms import EntidadeForm


@skip('Pulando testes de forms por causa do erro de BD')
class DestinationsEntidadeFormUnitTest(TestCase):
    @parameterized.expand([
        ('cnpj', 'Digite apenas números'),
        ('razao', 'Digite algo com pelo menos 10 caracteres aqui'),
    ])
    def test_field_placeholder_is_correct(self, field, placeholder):
        form = EntidadeForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)
