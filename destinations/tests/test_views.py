from django.test import TestCase
from django.urls import resolve, reverse

from destinations import views


class DestinationsViewsTests(TestCase):
    def test_destination_home_view_function_is_correct(self):
        view = resolve(reverse('destinations:home'))
        self.assertIs(views.home, view.func)

    def test_destination_entidades_insert_view_function_is_correct(self):
        view = resolve(reverse('destinations:entidade-insert'))
        self.assertIs(views.entidades_insert, view.func)

    def test_destination_entidade_update_view_function_is_correct(self):
        view = resolve(reverse('destinations:entidade-update'))
        self.assertIs(views.entidades_update, view.func)

    def test_destination_saidas_function_view_is_correct(self):
        view = resolve(reverse('destinations:saidas'))
        self.assertIs(views.saidas, view.func)

    def test_destination_registrodestino_view_function_is_correct(self):
        view = resolve(reverse('destinations:registrodestino'))
        self.assertIs(views.registrodestino, view.func)

    def test_destination_planilha_view_function_is_correct(self):
        view = resolve(reverse('destinations:planilha'))
        self.assertIs(views.planilha, view.func)

    def test_destinations_home_view_returns_status_code_200(self):
        url = reverse('destinations:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_destinations_entidade_insert_view_returns_status_code_200(self):
        url = reverse('destinations:entidade-insert')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_destinations_entidade_update_view_returns_status_code_200(self):
        url = reverse('destinations:entidade-update')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_destinations_saidas_view_returns_status_code_200(self):
        url = reverse('destinations:saidas')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_destinations_registrodestino_view_returns_status_code_200(self):
        url = reverse('destinations:registrodestino')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_destinations_template_home_is_correct(self):
        url = reverse('destinations:home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'destinations/pages/index.html')

    def test_destinations_template_entidade_insert_is_correct(self):
        url = reverse('destinations:entidade-insert')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'destinations/pages/entidades-insert.html')  # noqa: E501

    def test_destinations_template_entidade_update_is_correct(self):
        url = reverse('destinations:entidade-update')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'destinations/pages/entidades-update.html')  # noqa: E501

    def test_destinations_template_saidas_is_correct(self):
        url = reverse('destinations:saidas')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'destinations/pages/registro-saidas.html')  # noqa: E501

    def test_destinations_template_registrodestino_is_correct(self):
        url = reverse('destinations:registrodestino')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'destinations/pages/registro-destino.html')  # noqa: E501
