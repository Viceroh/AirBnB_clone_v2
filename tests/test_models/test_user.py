import unittest
from models.base_model import BaseModel, Base
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup a test database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Set up the test environment"""
        self.user = User(email="test@example.com", password="password123",
                         first_name="John", last_name="Doe")

    def test_instantiation(self):
        """Test that a user can be instantiated"""
        self.assertIsInstance(self.user, User)

    def test_email_attribute(self):
        """Test that the email attribute is set correctly"""
        self.assertEqual(self.user.email, "test@example.com")

    def test_password_attribute(self):
        """Test that the password attribute is set correctly"""
        self.assertEqual(self.user.password, "password123")

    def test_first_name_attribute(self):
        """Test that the first_name attribute is set correctly"""
        self.assertEqual(self.user.first_name, "John")

    def test_last_name_attribute(self):
        """Test that the last_name attribute is set correctly"""
        self.assertEqual(self.user.last_name, "Doe")

    def test_save(self):
        """Test that the save method updates the updated_at attribute"""
        initial_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary
        representation of the instance"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertNotIn('_sa_instance_state', user_dict)

    def tearDown(self):
        """Clean up the test environment"""
        session.close()


if __name__ == '__main__':
    unittest.main()
