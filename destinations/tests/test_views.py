from django.test import TestCase
from django.urls import resolve, reverse

from destinations import views


class DestinationsViewsTests(TestCase):
    def test_destination_home_function_is_correct(self):
        view = resolve(reverse('destinations:home'))
        self.assertIs(views.home, view.func)

    def test_destination_entidades_insert_function_is_correct(self):
        view = resolve(reverse('destinations:entidade-insert'))
        self.assertIs(views.entidades_insert, view.func)

    def test_destination_entidade_update_function_is_correct(self):
        view = resolve(reverse('destinations:entidade-update'))
        self.assertIs(views.entidades_update, view.func)

    def test_destination_saidas_function_is_correct(self):
        view = resolve(reverse('destinations:saidas'))
        self.assertIs(views.saidas, view.func)

    def test_destination_registrodestino_function_is_correct(self):
        view = resolve(reverse('destinations:registrodestino'))
        self.assertIs(views.registrodestino, view.func)

    def test_destination_planilha_function_is_correct(self):
        view = resolve(reverse('destinations:planilha'))
        self.assertIs(views.planilha, view.func)