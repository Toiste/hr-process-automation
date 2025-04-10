import pytest
from candidatos.models import Candidato

@pytest.mark.django_db
def test_candidato_criacao():
    candidato = Candidato.objects.create(
        nome="João",
        email="joao@email.com",
        telefone="99999-9999",
        experiencia="5 anos em Python",
        formacao="Ciência da Computação",
        pontuacao=88.5,
        vaga="Desenvolvedor Python"
    )
    assert candidato.pk is not None
    assert candidato.nome == "João"
