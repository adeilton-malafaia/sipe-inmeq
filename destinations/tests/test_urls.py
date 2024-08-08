from django.test import TestCase
from django.urls import reverse


class DestinationsURLsTests(TestCase):
    def test_destinations_home_url_is_correct(self):
        url = reverse('destinations:home')
        self.assertEqual(url, '/')

    def test_destinations_entidades_cadastro_url_is_correct(self):
        url = reverse('destinations:entidade-insert')
        self.assertEqual(url, '/entidades/cadastro/')

    def test_destinations_entidades_update_url_is_correct(self):
        url = reverse('destinations:entidade-update')
        self.assertEqual(url, '/entidades/atualizar/')

    def test_destinations_entidades_registrodestino_url_is_correct(self):
        url = reverse('destinations:registrodestino')
        self.assertEqual(url, '/entidades/registrodestino/')
