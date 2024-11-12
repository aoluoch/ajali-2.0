
import pytest
from models.user import User

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

def test_serialize_rules():
    """
    GIVEN a User model
    WHEN checking the serialize_rules attribute
    THEN ensure '-reports' is in the serialize_rules
    """
    assert User.serialize_rules == ('-reports',)

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
