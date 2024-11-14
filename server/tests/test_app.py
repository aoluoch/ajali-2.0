from app import app

def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!, Welcome to your work flow!"

from models.user import User

def test_user_fields():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the presence of the required fields
    """
    user = User()

    # Check the presence of fields in the User model (excluding relationships)
    assert hasattr(user, 'id')
    assert hasattr(user, 'username')
    assert hasattr(user, 'email')
    assert hasattr(user, 'password_hash')
    assert hasattr(user, 'is_admin')

    # Exclude checking the 'reports' relationship
    assert not hasattr(user, 'reports')


