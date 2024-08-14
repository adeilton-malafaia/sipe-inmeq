from django.test import TestCase
from destinations.models import Entidade

class DestinationsTestBase(TestCase):
    def createEntidade(
            self,
                cnpj='12345678901234',
                razao='Entidade Teste',
                nf='Entidade Teste',
                contatos='José',
                email='entidade@entidade.com',
                fones='82 3214 4123',
                validade='2025-06-30',
                ativo='s',
        ):
        Entidade.objects.create(
                    cnpj=cnpj,
                    razao=razao,
                    nf=nf,
                    contatos=contatos,
                    email=email,
                    fones=fones,
                    validade=validade,
                    ativo=ativo,
        )