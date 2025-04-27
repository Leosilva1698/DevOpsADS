
from unittest.mock import patch
from src.main import (
    root, funcaoteste, create_estudante,
    update_estudante, delete_estudante, Estudante
)


def test_root():
    assert root() == {"message": "Hello Word"}


def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()

    assert result == 12345


def test_create_estudante():
    estudante_teste = Estudante(name="Leonardo", curso="ADS", ativo=True)
    return estudante_teste == create_estudante(estudante_teste)


def test_update_estudante_negativo():
    assert not update_estudante(-5)


def test_update_estudante_postivo():
    assert update_estudante(10)


def test_delete_estudante_negativo():
    assert not delete_estudante(-5)


def test_delete_estudante_positivo():
    assert delete_estudante(5)
