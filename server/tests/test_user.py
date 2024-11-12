from models.user import User

def test_user_fields():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the presence of the required fields
    """
    user = User()
    assert hasattr(user, 'id')
    assert hasattr(user, 'username')
    assert hasattr(user, 'email')
    assert hasattr(user, 'password_hash')
    assert hasattr(user, 'is_admin')
    assert hasattr(user, 'reports')
