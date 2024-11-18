import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:ajali.db:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()

def test_register_user(client):
    response = client.post('/users', json={
        'username': 'testuser', 'email': 'test@example.com', 'password': 'password123'
    })
    assert response.status_code == 201

def test_login_user(client):
    client.post('/users', json={
        'username': 'testuser', 'email': 'test@example.com', 'password': 'password123'
    })
    response = client.post('/login', json={'username': 'testuser', 'password': 'password123'})
    assert response.status_code == 200

def test_create_incident(client):
    client.post('/users', json={
        'username': 'user', 'email': 'user@example.com', 'password': 'password'
    })
    client.post('/login', json={'username': 'user', 'password': 'password'})
    response = client.post('/incidents', json={
        'description': 'Test incident', 'latitude': 0.0, 'longitude': 0.0
    })
    assert response.status_code == 201

def test_get_incidents(client):
    client.post('/users', json={
        'username': 'user', 'email': 'user@example.com', 'password': 'password'
    })
    client.post('/login', json={'username': 'user', 'password': 'password'})
    response = client.get('/incidents')
    assert response.status_code == 200
