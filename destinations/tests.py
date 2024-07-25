from django.test import TestCase
from django.urls import reverse

# from django.urls import resolve

# from . import views


class DestinationsURLsTests(TestCase):
    def test_url_destinations_home_is_correct(self):
        url = reverse('destinations:home')
        self.assertEqual(url, '/')

    def test_url_destinations_entidades_cadastro_is_correct(self):
        url = reverse('destinations:entidade-insert')
        self.assertEqual(url, '/entidades/cadastro/')

    def test_url_destinations_entidades_update_is_correct(self):
        url = reverse('destinations:entidade-update')
        self.assertEqual(url, '/entidades/atualizar/')

    def test_url_destinations_entidades_registrodestino_is_correct(self):
        url = reverse('destinations:registrodestino')
        self.assertEqual(url, '/entidades/registrodestino/')


# class DestinationsViewsTests(TestCase):
#     def test_destination_home_function_is_correct(self):
#         view = resolve(reverse('destinations:home'))
#         self.assertIs(views.home, view)

#     def test_destination_entidades_insert_function_is_correct(self):
#         view = resolve(reverse('destinations:entidades_insert'))
#         self.assertIs(views.entidades_insert, view)

#     def test_destination_entidade_update_function_is_correct(self):
#         view = resolve(reverse('destinations:entidade_update'))
#         self.assertIs(views.entidades_update, view)

#     def test_destination_saidas_function_is_correct(self):
#         view = resolve(reverse('destinations:saidas'))
#         self.assertIs(views.saidas, view)

#     def test_destination_registrodestino_function_is_correct(self):
#         view = resolve(reverse('destinations:registrodestino'))
#         self.assertIs(views.registrodestino, view)

#     def test_destination_planilha_function_is_correct(self):
#         view = reverse('destinations:planilha')
#         self.assertIs(views.planilha, view)
