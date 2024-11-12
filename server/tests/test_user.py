import sys
from unittest.mock import Mock

# Mock sqlalchemy_serializer if it doesn't exist
sys.modules['sqlalchemy_serializer'] = Mock()

from models.user import User

def test_table_name():
    assert User.__tablename__ == 'users'

def test_user_fields():
    user = User()
    assert hasattr(user, 'id')
    assert hasattr(user, 'username')
    assert hasattr(user, 'email')
    assert hasattr(user, 'password_hash')
    assert hasattr(user, 'is_admin')
    assert hasattr(user, 'reports')
