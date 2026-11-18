
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
    assert b"TeleCampo" in resposta.data
    assert b"Consulta de Atendimento FTTH" in resposta.data


def test_consulta_atendimento_existente(client):
    resposta = client.get("/?codigo=FTTH-2026-001")

    assert resposta.status_code == 200
    assert b"FTTH-2026-001" in resposta.data
    assert b"PON-DEMO-001" in resposta.data
    assert b"ABERTO" in resposta.data


def test_consulta_atendimento_inexistente(client):
    resposta = client.get("/?codigo=FTTH-9999")

    assert resposta.status_code == 200
    assert "Atendimento não localizado." in resposta.get_data(
        as_text=True
    )


def test_verificacao_saude(client):
    resposta = client.get("/health")

    assert resposta.status_code == 200
    assert resposta.json["status"] == "ok"
    assert resposta.json["servico"] == "TeleCampo"
