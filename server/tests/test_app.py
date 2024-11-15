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

def test_user_model_serialization():
    # Create a dummy user object
    user = User(
        id=1,
        username="testuser",
        email="testuser@example.com",
        password_hash="hashedpassword",
        is_admin=True
    )

    # Serialize the user object
    serialized_user = user.to_dict()

    # Check if serialized data matches the expected output
    assert serialized_user["id"] == 1, "Serialized user should have the correct 'id'"
    assert serialized_user["username"] == "testuser", "Serialized user should have the correct 'username'"
    assert serialized_user["email"] == "testuser@example.com", "Serialized user should have the correct 'email'"
    assert "password_hash" not in serialized_user, "'password_hash' should not be serialized"
    assert "reports" not in serialized_user, "'reports' should not be serialized due to serialize_rules"
    assert serialized_user["is_admin"] is True, "Serialized user should have the correct 'is_admin'"



