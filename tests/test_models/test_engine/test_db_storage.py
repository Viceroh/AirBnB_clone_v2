import unittest
from unittest.mock import patch, MagicMock
from models.engine.db_storage import DBStorage

class TestDBStorage(unittest.TestCase):
    def setUp(self):
        self.db_storage = DBStorage()

    @patch('models.engine.db_storage.create_engine')
    @patch('models.engine.db_storage.scoped_session')
    def test_new(self, mock_scoped_session, mock_create_engine):
        mock_session = MagicMock()
        mock_scoped_session.return_value = mock_session
        self.db_storage.reload()  # Reload to initialize session
        obj = object()
        self.db_storage.new(obj)
        self.assertTrue(mock_session.add.called)

    @patch('models.engine.db_storage.create_engine')
    @patch('models.engine.db_storage.scoped_session')
    def test_save(self, mock_scoped_session, mock_create_engine):
        mock_session = MagicMock()
        mock_scoped_session.return_value = mock_session
        self.db_storage.reload()  # Reload to initialize session
        obj = object()
        self.db_storage.new(obj)
        self.db_storage.save()
        self.assertTrue(mock_session.commit.called)

    @patch('models.engine.db_storage.create_engine')
    @patch('models.engine.db_storage.scoped_session')
    def test_delete(self, mock_scoped_session, mock_create_engine):
        mock_session = MagicMock()
        mock_scoped_session.return_value = mock_session
        self.db_storage.reload()  # Reload to initialize session
        obj = object()
        self.db_storage.new(obj)
        self.db_storage.delete(obj)
        self.assertTrue(mock_session.delete.called)

    @patch('models.engine.db_storage.create_engine')
    @patch('models.engine.db_storage.scoped_session')
    def test_reload(self, mock_scoped_session, mock_create_engine):
        mock_session = MagicMock()
        mock_scoped_session.return_value = mock_session
        self.db_storage.reload()
        self.assertTrue(mock_session.close.called)

    @patch('models.engine.db_storage.os.environ', {
        "HBNB_ENV": "test",
        "HBNB_MYSQL_USER": "test_user",
        "HBNB_MYSQL_PWD": "test_pwd",
        "HBNB_MYSQL_HOST": "test_host",
        "HBNB_MYSQL_DB": "test_db"
    })
    @patch('models.engine.db_storage.create_engine')
    @patch('models.engine.db_storage.Base.metadata')
    @patch('models.engine.db_storage.scoped_session')
    def test_init_with_test_env(self, mock_scoped_session, mock_metadata, mock_create_engine, mock_os_environ):
        mock_session = MagicMock()
        mock_scoped_session.return_value = mock_session
        self.db_storage = DBStorage()
        self.assertTrue(mock_create_engine.called)
        self.assertTrue(mock_metadata.drop_all.called)

    def tearDown(self):
        self.db_storage.close()

if __name__ == '__main__':
    unittest.main()
