from models.user import User

def test_user_model_fields():
    # Check if the fields exist in the User model
    assert hasattr(User, 'id'), "User model should have an 'id' field"
    assert hasattr(User, 'username'), "User model should have a 'username' field"
    assert hasattr(User, 'email'), "User model should have an 'email' field"
    assert hasattr(User, 'password_hash'), "User model should have a 'password_hash' field"
    assert hasattr(User, 'reports'), "User model should have a 'reports' relationship"

def test_sqlalchemy_serializer_mixin():
    # Check if SerializerMixin is correctly integrated
    assert hasattr(User, 'to_dict'), "User model should have a 'to_dict' method from SerializerMixin"
    assert hasattr(User, 'serialize_rules'), "User model should have 'serialize_rules' from SerializerMixin"
    assert isinstance(User.serialize_rules, tuple), "'serialize_rules' should be a tuple"
    assert '-reports' in User.serialize_rules, "'serialize_rules' should include '-reports' to exclude 'reports' from serialization"