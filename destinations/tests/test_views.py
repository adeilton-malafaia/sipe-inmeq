# from unittest import skip

from django.test import TestCase
from django.urls import resolve, reverse

from destinations.views import home


# @skip('Pulando testes de views por causa do erro de bd')
class DestinationsViewsTests(TestCase):
    def test_destination_home_function_is_correct(self):
        view = resolve(reverse('destinations:home'))
        self.assertIs(home, view)

    # def test_destination_entidades_insert_function_is_correct(self):
    #     view = resolve(reverse('destinations:entidades_insert'))
    #     self.assertIs(views.entidades_insert, view)

    # def test_destination_entidade_update_function_is_correct(self):
    #     view = resolve(reverse('destinations:entidade_update'))
    #     self.assertIs(views.entidades_update, view)

    # def test_destination_saidas_function_is_correct(self):
    #     view = resolve(reverse('destinations:saidas'))
    #     self.assertIs(views.saidas, view)

    # def test_destination_registrodestino_function_is_correct(self):
    #     view = resolve(reverse('destinations:registrodestino'))
    #     self.assertIs(views.registrodestino, view)

    # def test_destination_planilha_function_is_correct(self):
    #     view = reverse('destinations:planilha')
    #     self.assertIs(views.planilha, view)

    # def test_destination_home_returns_correct_template(self):
    #     response = self.client.get(reverse('destinations:home'))
    #     self.assertEqual(response.status_code, 200)
