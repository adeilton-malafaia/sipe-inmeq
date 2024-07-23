from django.test import TestCase
from destinations.forms import EntidadeForm
from parameterized import parameterized

class DestinationsEntidadeFormUnitTest(TestCase):
    @parameterized.expand([
        ('cnpj', 'Digite apeeenas números'),
        ('razao', 'Digite algo com pelo menos 10 caracteres aqui'),
    ])

    def test_field_placeholder_is_correct(self, field, placeholder):
        form = EntidadeForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)