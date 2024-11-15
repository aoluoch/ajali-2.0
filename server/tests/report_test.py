import pytest
from models.incident_report import db, IncidentReport
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='module')
def setup_db():
    """Setup an in-memory database for testing."""
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()

def test_incident_report_model_fields(setup_db):
    # Ensure the columns in the IncidentReport model exist
    incident_report = IncidentReport()

    assert hasattr(incident_report, 'id')
    assert isinstance(incident_report.id, db.Integer)

    assert hasattr(incident_report, 'user_id')
    assert isinstance(incident_report.user_id, db.Integer)

    assert hasattr(incident_report, 'description')
    assert isinstance(incident_report.description, db.Text)

    assert hasattr(incident_report, 'status')
    assert isinstance(incident_report.status, db.String)

    assert hasattr(incident_report, 'latitude')
    assert isinstance(incident_report.latitude, db.Float)

    assert hasattr(incident_report, 'longitude')
    assert isinstance(incident_report.longitude, db.Float)

    assert hasattr(incident_report, 'created_at')
    assert isinstance(incident_report.created_at, db.DateTime)

    assert hasattr(incident_report, 'updated_at')
    assert isinstance(incident_report.updated_at, db.DateTime)

def test_incident_report_serialization(setup_db):
    # Test the serialization rules
    incident_report = IncidentReport()

    # Check serialization rules are correctly set
    assert '-user' in incident_report.serialize_rules
    assert '-images' in incident_report.serialize_rules
    assert '-videos' in incident_report.serialize_rules

def test_incident_report_invalid_data(setup_db):
    """Test for required fields (e.g., user_id, description, latitude, longitude)."""
    with pytest.raises(IntegrityError):
        incident_report = IncidentReport(user_id=None, description="Test description", latitude=0.0, longitude=0.0)
        db.session.add(incident_report)
        db.session.commit()

    with pytest.raises(IntegrityError):
        incident_report = IncidentReport(user_id=1, description=None, latitude=0.0, longitude=0.0)
        db.session.add(incident_report)
        db.session.commit()

def test_incident_report_default_status(setup_db):
    """Test the default value for status column."""
    incident_report = IncidentReport(user_id=1, description="Test description", latitude=0.0, longitude=0.0)
    db.session.add(incident_report)
    db.session.commit()
    
    assert incident_report.status == 'under investigation'
