from models.user import User

def test_table_name():
    """
    GIVEN a User model
    WHEN checking the table name
    THEN ensure it is 'users'
    """
    assert User.__tablename__ == 'users'

def test_user_fields():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the presence of the fields
    """
    user = User()
    assert hasattr(user, 'id')
    assert hasattr(user, 'username')
    assert hasattr(user, 'email')
    assert hasattr(user, 'password_hash')
    assert hasattr(user, 'is_admin')
    assert hasattr(user, 'reports')
