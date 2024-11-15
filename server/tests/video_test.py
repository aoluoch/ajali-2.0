from models.incident_video import IncidentVideo

def test_incident_video_fields():
    """Test that the IncidentVideo model has the required fields"""
    # List of expected fields
    fields = ['id', 'report_id', 'video_url', 'incident']

    for field in fields:
        assert hasattr(IncidentVideo, field), f"Missing field: {field}"

def test_serializer_rules():
    """Test that the serializer rules are set correctly"""
    # Check if the model has 'serialize_rules' and its value
    assert hasattr(IncidentVideo, 'serialize_rules'), "Missing serialize_rules attribute"
    assert IncidentVideo.serialize_rules == ('-incident',), "serialize_rules attribute is not set correctly"
