
from unittest.mock import patch
from src.main import (
    root, funcaoteste, create_estudante,
    update_estudante, delete_estudante, Estudante
)
import pytest


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello Word"}


@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()
    assert result == 12345


@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Leonardo", curso="ADS", ativo=True)
    result = await create_estudante(estudante_teste)

    return estudante_teste == result


@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)

    assert not result


@pytest.mark.asyncio
async def test_update_estudante_postivo():
    result = await update_estudante(10)

    assert result


@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)

    assert not result


@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(5)

    assert result
