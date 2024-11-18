from models.incident_image import IncidentImage

def test_incident_image_model_fields():
    # Check if the fields exist in the IncidentImage model
    assert hasattr(IncidentImage, 'id'), "IncidentImage model should have an 'id' field"
    assert hasattr(IncidentImage, 'report_id'), "IncidentImage model should have a 'report_id' field"
    assert hasattr(IncidentImage, 'image_url'), "IncidentImage model should have an 'image_url' field"

def test_incident_image_relationship():
    # Check if the relationship exists in the IncidentImage model
    assert hasattr(IncidentImage, 'incident'), "IncidentImage model should have an 'incident' relationship"