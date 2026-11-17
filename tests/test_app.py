
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_pagina_inicial(client):
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert resposta.json["projeto"] == "TeleCampo"
    assert resposta.json["versao"] == "0.1.0"


def test_verificacao_saude(client):
    resposta = client.get("/health")

    assert resposta.status_code == 200
    assert resposta.json["status"] == "ok"
    assert resposta.json["servico"] == "TeleCampo"
