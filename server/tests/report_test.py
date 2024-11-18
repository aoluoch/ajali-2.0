from models.incident_report import IncidentReport

def test_incident_report_model_fields():
    # Check if the fields exist in the IncidentReport model
    assert hasattr(IncidentReport, 'id'), "IncidentReport model should have an 'id' field"
    assert hasattr(IncidentReport, 'user_id'), "IncidentReport model should have a 'user_id' field"
    assert hasattr(IncidentReport, 'description'), "IncidentReport model should have a 'description' field"
    assert hasattr(IncidentReport, 'status'), "IncidentReport model should have a 'status' field"
    assert hasattr(IncidentReport, 'latitude'), "IncidentReport model should have a 'latitude' field"
    assert hasattr(IncidentReport, 'longitude'), "IncidentReport model should have a 'longitude' field"
    assert hasattr(IncidentReport, 'created_at'), "IncidentReport model should have a 'created_at' field"
    assert hasattr(IncidentReport, 'updated_at'), "IncidentReport model should have an 'updated_at' field"

def test_incident_report_relationships():
    # Check if relationships exist in the IncidentReport model
    assert hasattr(IncidentReport, 'user'), "IncidentReport model should have a 'user' relationship"
    assert hasattr(IncidentReport, 'images'), "IncidentReport model should have an 'images' relationship"
    assert hasattr(IncidentReport, 'videos'), "IncidentReport model should have a 'videos' relationship"
