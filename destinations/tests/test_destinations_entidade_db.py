from django.test import TestCase

from destinations.models import Entidade


class TestDestinationEntidadeDB(TestCase):
    def getEntidade(
        self,
        cnpj='12345678901234',
        razao='Entidade Teste',
        validade='2026-08-05'
    ):
        return Entidade.objects.create(
            cnpj=cnpj,
            razao=razao,
            validade=validade
        )

    def test_maxlenght(self):
        ...
