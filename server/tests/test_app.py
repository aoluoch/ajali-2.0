from app import app

def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!, Welcome to your work flow!"

from models.user import User

def test_user_model_fields():
    # Check if the fields exist
    assert hasattr(User, 'id'), "User model should have an 'id' field"
    assert hasattr(User, 'username'), "User model should have a 'username' field"
    assert hasattr(User, 'email'), "User model should have an 'email' field"
    assert hasattr(User, 'password_hash'), "User model should have a 'password_hash' field"
    assert hasattr(User, 'is_admin'), "User model should have an 'is_admin' field"
    assert hasattr(User, 'reports'), "User model should have a 'reports' relationship"


