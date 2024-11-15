from models.incident_video import IncidentVideo

def test_incident_video_fields():
    """Test that the IncidentVideo model has the required fields"""
    fields = {
        'id': int,
        'report_id': int,
        'video_url': str,
        'incident': object,  # The relationship is an object
    }

    for field_name, field_type in fields.items():
        assert hasattr(IncidentVideo, field_name), f"Missing field: {field_name}"
        assert isinstance(getattr(IncidentVideo, field_name), field_type), f"Field {field_name} is not of type {field_type}"

def test_serializer_rules():
    """Test that the serializer rules are set correctly"""
    assert hasattr(IncidentVideo, 'serialize_rules'), "Missing serialize_rules attribute"
    assert IncidentVideo.serialize_rules == ('-incident',), "serialize_rules attribute is not set correctly"

def test_tablename():
    """Test that the table name is set correctly"""
    assert hasattr(IncidentVideo, '__tablename__'), "Missing __tablename__ attribute"
    assert IncidentVideo.__tablename__ == 'incident_videos', "__tablename__ is not set correctly"
