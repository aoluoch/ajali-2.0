import unittest
from models.incident_video import IncidentVideo


class TestIncidentVideoModel(unittest.TestCase):
    def test_fields_present(self):
        """Test that the IncidentVideo model has the required fields"""
        fields = {
            'id': int,
            'report_id': int,
            'video_url': str,
            'incident': object,  # The relationship is an object
        }

        for field_name, field_type in fields.items():
            self.assertTrue(hasattr(IncidentVideo, field_name), f"Missing field: {field_name}")
            self.assertTrue(
                isinstance(getattr(IncidentVideo, field_name), field_type),
                f"Field {field_name} is not of type {field_type}"
            )

    def test_serializer_rules(self):
        """Test that the serializer rules are set correctly"""
        self.assertTrue(hasattr(IncidentVideo, 'serialize_rules'), "Missing serialize_rules attribute")
        self.assertEqual(
            IncidentVideo.serialize_rules, ('-incident',),
            "serialize_rules attribute is not set correctly"
        )

    def test_tablename(self):
        """Test that the table name is set correctly"""
        self.assertTrue(hasattr(IncidentVideo, '__tablename__'), "Missing __tablename__ attribute")
        self.assertEqual(IncidentVideo.__tablename__, 'incident_videos', "__tablename__ is not set correctly")


if __name__ == '__main__':
    unittest.main()
