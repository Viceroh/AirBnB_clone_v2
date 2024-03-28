import unittest
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup a test database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class TestState(unittest.TestCase):
    """Test the State class"""

    def setUp(self):
        """Set up the test environment"""
        self.state = State(name="New York")

    def test_instantiation(self):
        """Test that a state can be instantiated"""
        self.assertIsInstance(self.state, State)

    def test_name_attribute(self):
        """Test that the name attribute is set correctly"""
        self.assertEqual(self.state.name, "New York")

    def test_save(self):
        """Test that the save method updates the updated_at attribute"""
        initial_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary
        representation of the instance"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['name'], "New York")
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertNotIn('_sa_instance_state', state_dict)

    def tearDown(self):
        """Clean up the test environment"""
        session.close()


if __name__ == '__main__':
    unittest.main()
