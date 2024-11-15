import pytest
from models.incident_report import IncidentReport
from models.extensions import db


@pytest.fixture(scope='module')
def setup_db():
    """Set up an in-memory database for testing."""
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


def test_incident_report_columns(setup_db):
    """Test to check if IncidentReport model has the correct fields defined."""
    
    # Get the column names from the IncidentReport model's table
    column_names = [column.name for column in IncidentReport.__table__.columns]
    
    # Define the expected column names
    expected_columns = [
        'id', 'user_id', 'description', 'status', 'latitude', 'longitude', 'created_at', 'updated_at'
    ]
    
    # Assert that each expected column exists in the model's table
    for column in expected_columns:
        assert column in column_names, f"Column '{column}' is missing from the IncidentReport model."


def test_incident_report_default_status(setup_db):
    """Test to check if the default status is set to 'under investigation'."""
    
    # Directly check the default value for the 'status' column in the model
    status_column = IncidentReport.__table__.columns['status']
    assert status_column.default.arg == 'under investigation', \
        f"Expected default value for 'status' to be 'under investigation', but got {status_column.default.arg}"
