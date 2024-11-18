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

def test_incident_report_sqlalchemy_serializer_mixin():
    # Check if SerializerMixin is correctly integrated in IncidentReport
    assert hasattr(IncidentReport, 'to_dict'), "IncidentReport model should have a 'to_dict' method from SerializerMixin"
    assert hasattr(IncidentReport, 'serialize_rules'), "IncidentReport model should have 'serialize_rules' from SerializerMixin"
    assert isinstance(IncidentReport.serialize_rules, tuple), "'serialize_rules' should be a tuple"
    assert '-user' in IncidentReport.serialize_rules, "'serialize_rules' should include '-user' to exclude 'user' from serialization"
    assert '-images' in IncidentReport.serialize_rules, "'serialize_rules' should include '-images' to exclude 'images' from serialization"
    assert '-videos' in IncidentReport.serialize_rules, "'serialize_rules' should include '-videos' to exclude 'videos' from serialization"

def test_incident_report_status_default():
    # Check if the default value of 'status' is correct
    report = IncidentReport()
    assert report.status == 'under investigation', "Default value of 'status' should be 'under investigation'"

def test_incident_report_created_updated_timestamps():
    # Check if 'created_at' and 'updated_at' fields behave correctly
    report = IncidentReport()
    assert report.created_at is not None, "'created_at' should have a default value"
    assert report.updated_at is None, "'updated_at' should be None initially"
