
from unittest.mock import patch
from src.main import (
    root, funcaoteste, create_estudante,
    update_estudante, delete_estudante, Estudante
)


def test_root():
    result = root()
    yield result
    assert result == {"message": "Hello Word"}


def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()
        yield result
    assert result == 12345


def test_create_estudante():
    estudante_teste = Estudante(name="Leonardo", curso="ADS", ativo=True)
    result = create_estudante(estudante_teste)
    yield result
    return estudante_teste == result


def test_update_estudante_negativo():
    result = update_estudante(-5)
    yield result
    assert not result


def test_update_estudante_postivo():
    result = update_estudante(10)
    yield result
    assert result


def test_delete_estudante_negativo():
    result = delete_estudante(-5)
    yield result
    assert not result


def test_delete_estudante_positivo():
    result = delete_estudante(5)
    yield result
    assert result
