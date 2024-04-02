import unittest
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup a test database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """Set up the test environment"""
        self.amenity = Amenity(name="WiFi")

    def test_instantiation(self):
        """Test that an amenity can be instantiated"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_name_attribute(self):
        """Test that the name attribute is set correctly"""
        self.assertEqual(self.amenity.name, "WiFi")

    def test_save(self):
        """Test that the save method updates the updated_at attribute"""
        initial_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary
        representation of the instance"""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['name'], "WiFi")
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertNotIn('_sa_instance_state', amenity_dict)


if __name__ == '__main__':
    unittest.main()
