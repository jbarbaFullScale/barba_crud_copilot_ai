import unittest
from app import app, db
from models import Contact

class ContactTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client and initialize a test database."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        """Clean up after each test."""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_contact(self):
        """Test creating a new contact."""
        response = self.app.post('/create', data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'address': '123 Main St',
            'contact_number': '1234567890'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with app.app_context():
            contact = Contact.query.first()
            self.assertIsNotNone(contact)
            self.assertEqual(contact.name, 'John Doe')

    def test_read_contacts(self):
        """Test retrieving the list of contacts."""
        with app.app_context():
            contact = Contact(name='Jane Doe', email='jane@example.com', address='456 Elm St', contact_number='9876543210')
            db.session.add(contact)
            db.session.commit()
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jane Doe', response.data)

    def test_update_contact(self):
        """Test updating an existing contact."""
        with app.app_context():
            contact = Contact(name='Jane Doe', email='jane@example.com', address='456 Elm St', contact_number='9876543210')
            db.session.add(contact)
            db.session.commit()
            contact_id = contact.id
        response = self.app.post(f'/update/{contact_id}', data={
            'name': 'Jane Smith',
            'email': 'jane.smith@example.com',
            'address': '789 Oak St',
            'contact_number': '1112223333'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with app.app_context():
            contact = Contact.query.get(contact_id)
            self.assertEqual(contact.name, 'Jane Smith')

    def test_delete_contact(self):
        """Test deleting a contact."""
        with app.app_context():
            contact = Contact(name='Jane Doe', email='jane@example.com', address='456 Elm St', contact_number='9876543210')
            db.session.add(contact)
            db.session.commit()
            contact_id = contact.id
        response = self.app.post(f'/delete/{contact_id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with app.app_context():
            contact = Contact.query.get(contact_id)
            self.assertIsNone(contact)

    def test_create_contact(self):
        """Test creating a new contact."""
        response = self.app.post('/create', data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'address': '123 Main St',
            'contact_number': '1234567890'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with app.app_context():
            contact = Contact.query.first()
            self.assertIsNotNone(contact)
            self.assertEqual(contact.name, 'John Doe')

if __name__ == '__main__':
    unittest.main()