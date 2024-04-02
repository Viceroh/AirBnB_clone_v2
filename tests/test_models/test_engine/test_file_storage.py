import unittest
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage  # Replace 'your_module' with the actual module name

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.storage = FileStorage()
        self.user = User()
        self.place = Place()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.review = Review()

    @patch('builtins.open', new_callable=mock_open, read_data='{"User.1": {"__class__": "User", "id": "1"}}')
    def test_reload(self, mock_file):
        """Test the reload method"""
        self.storage.reload()
        self.assertIn('User.1', self.storage.all())

    @patch('builtins.open', new_callable=mock_open)
    def test_save(self, mock_file):
        """Test the save method"""
        self.storage.new(self.user)
        self.storage.save()
        # Check that write was called at least once
        mock_file().write.assert_called()

    def test_new(self):
        """Test the new method"""
        self.storage.new(self.user)
        self.assertIn(self.user.to_dict()['__class__'] + '.' + self.user.id, self.storage.all())

    def test_delete(self):
        """Test the delete method"""
        self.storage.new(self.user)
        self.storage.delete(self.user)
        self.assertNotIn(self.user.to_dict()['__class__'] + '.' + self.user.id, self.storage.all())

    def test_all(self):
        """Test the all method"""
        self.storage.new(self.user)
        self.storage.new(self.place)
        all_objects = self.storage.all()
        self.assertIn(self.user.to_dict()['__class__'] + '.' + self.user.id, all_objects)
        self.assertIn(self.place.to_dict()['__class__'] + '.' + self.place.id, all_objects)

        # Test filtering by class
        user_objects = self.storage.all(cls=User)
        self.assertIn(self.user.to_dict()['__class__'] + '.' + self.user.id, user_objects)
        self.assertNotIn(self.place.to_dict()['__class__'] + '.' + self.place.id, user_objects)

if __name__ == '__main__':
    unittest.main()
