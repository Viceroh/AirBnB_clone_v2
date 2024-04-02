import unittest
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup a test database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class TestPlace(unittest.TestCase):
    """Test the Place class"""

    def setUp(self):
        """Set up the test environment"""
        self.place = Place(name="Test Place", city_id="NY", user_id="user123",
                           number_rooms=2, number_bathrooms=1, max_guest=4,
                           price_by_night=100,
                           latitude=40.7128,
                           longitude=-74.0060)

    def test_instantiation(self):
        """Test that a place can be instantiated"""
        self.assertIsInstance(self.place, Place)

    def test_name_attribute(self):
        """Test that the name attribute is set correctly"""
        self.assertEqual(self.place.name, "Test Place")

    def test_city_id_attribute(self):
        """Test that the city_id attribute is set correctly"""
        self.assertEqual(self.place.city_id, "NY")

    def test_user_id_attribute(self):
        """Test that the user_id attribute is set correctly"""
        self.assertEqual(self.place.user_id, "user123")

    def test_save(self):
        """Test that the save method updates the updated_at attribute"""
        initial_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary
        representation of the instance"""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['name'], "Test Place")
        self.assertEqual(place_dict['city_id'], "NY")
        self.assertEqual(place_dict['user_id'], "user123")
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertNotIn('_sa_instance_state', place_dict)

    def tearDown(self):
        """Clean up the test environment"""
        session.close()


if __name__ == '__main__':
    unittest.main()
