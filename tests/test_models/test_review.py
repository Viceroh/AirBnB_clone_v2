import unittest
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup a test database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def setUp(self):
        """Set up the test environment"""
        self.review = Review(text="Great place!",
                             place_id="place123", user_id="user456")

    def test_instantiation(self):
        """Test that a review can be instantiated"""
        self.assertIsInstance(self.review, Review)

    def test_text_attribute(self):
        """Test that the text attribute is set correctly"""
        self.assertEqual(self.review.text, "Great place!")

    def test_place_id_attribute(self):
        """Test that the place_id attribute is set correctly"""
        self.assertEqual(self.review.place_id, "place123")

    def test_user_id_attribute(self):
        """Test that the user_id attribute is set correctly"""
        self.assertEqual(self.review.user_id, "user456")

    def test_save(self):
        """Test that the save method updates the updated_at attribute"""
        initial_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary
        representation of the instance"""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['text'], "Great place!")
        self.assertEqual(review_dict['place_id'], "place123")
        self.assertEqual(review_dict['user_id'], "user456")
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertNotIn('_sa_instance_state', review_dict)

    def tearDown(self):
        """Clean up the test environment"""
        session.close()


if __name__ == '__main__':
    unittest.main()
