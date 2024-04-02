import unittest
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup a test database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class TestCity(unittest.TestCase):
    """Test the City class"""

    def setUp(self):
        """Set up the test environment"""
        self.city = City(name="New York", state_id="NY")

    def test_instantiation(self):
        """Test that a city can be instantiated"""
        self.assertIsInstance(self.city, City)

    def test_name_attribute(self):
        """Test that the name attribute is set correctly"""
        self.assertEqual(self.city.name, "New York")

    def test_state_id_attribute(self):
        """Test that the state_id attribute is set correctly"""
        self.assertEqual(self.city.state_id, "NY")

    def test_save(self):
        """Test that the save method updates the updated_at attribute"""
        initial_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary
        representation of the instance"""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['name'], "New York")
        self.assertEqual(city_dict['state_id'], "NY")
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertNotIn('_sa_instance_state', city_dict)

    def tearDown(self):
        """Clean up the test environment"""
        session.close()


if __name__ == '__main__':
    unittest.main()
