import pytest
from app import app, realizaConsulta


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_realizaConsulta():
    query = "SELECT * FROM Tbpessoa"
    resultado = realizaConsulta(query)
    assert isinstance(resultado, list)
    assert len(resultado) > 0


def test_teste(client):
    response = client.get("/teste")
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data


def test_base(client):
    response = client.get("/base")
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data


def test_consultas(client):
    response = client.get("/consultas")
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data


def test_deletarConsulta(client):
    response = client.get("/consultas/deletarConsulta/1,2,3")
    assert response.status_code == 200
    # Adicione asserções para verificar o comportamento esperado da função deletarConsulta


def test_filtrarConsulta(client):
    response = client.get("/consultas/filtrarConsulta/valor1,valor2,valor3")
    assert response.status_code == 200
    # Adicione asserções para verificar o comportamento esperado da função filtrarConsulta


def test_medicos(client):
    response = client.get("/medicos")
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data


def test_cadastroMedico(client):
    response = client.get("/cadastroMedico")
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data


def test_cadastroPaciente(client):
    response = client.get("/cadastroPaciente")
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data
