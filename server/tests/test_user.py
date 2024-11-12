import pytest
from models import db, User

@pytest.fixture(scope='module')
def new_user():
    # Create a sample user instance for testing
    return User(
        username="testuser",
        email="testuser@example.com",
        password_hash="hashed_password_123",
        is_admin=True
    )

def test_table_name():
    """
    GIVEN a User model
    WHEN checking the table name
    THEN ensure it is 'users'
    """
    assert User.__tablename__ == 'users'

def test_user_fields(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the presence of the fields
    """
    assert hasattr(new_user, 'id')
    assert hasattr(new_user, 'username')
    assert hasattr(new_user, 'email')
    assert hasattr(new_user, 'password_hash')
    assert hasattr(new_user, 'is_admin')
    assert hasattr(new_user, 'reports')
