import pytest
from app import app, db
from models.user import User
from models.incident_report import IncidentReport

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()

def test_user_registration(client):
    response = client.post('/users', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'User created successfully'

def test_user_login(client):
    client.post('/users', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Login successful'

def test_session_check(client):
    client.post('/users', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    client.post('/login', json={
        'username': 'testuser',
        'password': 'password123'
    })
    response = client.get('/check_session')
    assert response.status_code == 200
    assert response.json['name'] == 'testuser'

def test_create_incident(client):
    client.post('/users', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    client.post('/login', json={
        'username': 'testuser',
        'password': 'password123'
    })
    response = client.post('/incidents', json={
        'description': 'Test incident',
        'latitude': -1.2921,
        'longitude': 36.8219
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Incident created successfully'
