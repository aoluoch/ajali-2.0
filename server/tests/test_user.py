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
    assert not hasattr(user, 'reports')  # Ensure 'reports' is not part of the test

