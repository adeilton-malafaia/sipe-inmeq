from django.test import TestCase
from django.urls import reverse


class DestinationsURLsTests(TestCase):
    def test_url_destinations_home_is_correct(self):
        url = reverse('destinations:entidade-insert')
        self.assertEqual(url, '/entidades/cadastro/')

    def test_url_destinations_entidades_cadastro_is_correct(self):
        url = reverse('destinations:entidade-insert')
        self.assertEqual(url, '/entidades/cadastro/')

    def test_url_destinations_entidades_update_is_correct(self):
        url = reverse('destinations:entidade-update')
        self.assertEqual(url, '/entidades/atualizar/')

    def test_url_destinations_entidades_registrodestino_is_correct(self):
        url = reverse('destinations:entidade-registrodestino')
        self.assertEqual(url, '/entidades/registrodestino/')
