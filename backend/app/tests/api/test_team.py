from fastapi.testclient import TestClient
from app.main import app  # Importa tu instancia de FastAPI
from app.schemas.team import TeamCreate
from app.db.setup import async_session
from app.db.models.team import Team  # Importa tu modelo de datos

client = TestClient(app)

# Define datos de prueba
test_team_data: TeamCreate = {
    "name": "Test Team",
    "location": "Test Location"
}


def test_create_team():
    response = client.post("/teams/", json=test_team_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == test_team_data["name"]
    assert data["description"] == test_team_data["description"]

    # Limpia los datos de prueba
    with async_session() as session:
        team = session.query(Team).filter_by(id=data["id"]).first()
        session.delete(team)


def test_read_teams():
    response = client.get("/teams/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_team():
    # Crea un equipo de prueba primero
    with async_session() as session:
        team = Team(**test_team_data)
        session.add(team)
        session.commit()
        session.refresh(team)

    response = client.get(f"/teams/{team.id}")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == test_team_data["name"]
    assert data["description"] == test_team_data["description"]

    # Limpia los datos de prueba
    with async_session() as session:
        team = session.query(Team).filter_by(id=team.id).first()
        session.delete(team)


def test_update_team():
    # Crea un equipo de prueba primero
    with async_session() as session:
        team = Team(**test_team_data)
        session.add(team)
        session.commit()
        session.refresh(team)

    update_data = {
        "name": "Updated Team Name",
        "description": "Updated description."
    }

    response = client.patch(f"/teams/{team.id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == update_data["name"]
    assert data["description"] == update_data["description"]

    # Limpia los datos de prueba
    with async_session() as session:
        team = session.query(Team).filter_by(id=team.id).first()
        session.delete(team)
