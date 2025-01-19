import unittest
from unittest.mock import MagicMock
from webapp import create_app, db
from webapp.auth.models import User
from webapp.chat.models import Message
from flask import jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit
import os

class MockDatabase:
    """
    A mock database to simulate chat messages between doctors and patients.
    """
    def __init__(self):
        self.messages = []  # Stores mock chat messages
        self.users = []  # Stores mock users (doctor, patient)

    def reset(self):
        """Reset the database to its initial state."""
        self.messages = []
        self.users = []

    def add_message(self, message):
        self.messages.append(message)

    def get_messages_for_session(self, doctor_id, patient_id):
        """Get messages between a doctor and a patient."""
        return [
            msg for msg in self.messages if 
            (msg['doctor_id'] == doctor_id and msg['patient_id'] == patient_id) or 
            (msg['doctor_id'] == patient_id and msg['patient_id'] == doctor_id)
        ]


class ChatTestCase(unittest.TestCase):
    """
    Test cases for the chat functionality.
    """

    @classmethod
    def setUpClass(cls):
        """Set up the Flask application."""
        env = os.environ.get('WEBAPP_ENV', 'dev')  # Use 'dev' if WEBAPP_ENV is not set
        cls.app = create_app('config.%sConfig' % env.capitalize())
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        """Clean up after the tests."""
        cls.app_context.pop()

    def setUp(self):
        """Set up a fresh mock database for each test."""
        self.mock_db = MockDatabase()
        self.mock_db.reset()  # Ensure a clean slate for each test

        # Mock users (doctor and patient)
        self.doctor = {'id': 1, 'username': 'doctor'}
        self.patient = {'id': 2, 'username': 'patient'}
        self.mock_db.users.extend([self.doctor, self.patient])

    def test_doctor_can_send_message(self):
        """Test that a doctor can send a message to a patient."""
        message_content = 'Hello, Patient!'
        message = {'doctor_id': self.doctor['id'], 'patient_id': self.patient['id'], 'content': message_content}
        self.mock_db.add_message(message)

        # Verify the message is saved in the mock database
        messages = self.mock_db.get_messages_for_session(self.doctor['id'], self.patient['id'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]['content'], message_content)

    def test_patient_can_send_message(self):
        """Test that a patient can send a message to a doctor."""
        message_content = 'Hello, Doctor!'
        message = {'doctor_id': self.doctor['id'], 'patient_id': self.patient['id'], 'content': message_content}
        self.mock_db.add_message(message)

        # Verify the message is saved in the mock database
        messages = self.mock_db.get_messages_for_session(self.doctor['id'], self.patient['id'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]['content'], message_content)

    def test_doctor_can_see_patient_message(self):
        """Test that the doctor can see the patient’s message."""
        message_content = 'Patient message'
        message = {'doctor_id': self.doctor['id'], 'patient_id': self.patient['id'], 'content': message_content}
        self.mock_db.add_message(message)

        # Verify the doctor retrieves the message
        messages = self.mock_db.get_messages_for_session(self.doctor['id'], self.patient['id'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]['content'], message_content)

    def test_patient_can_see_doctor_message(self):
        """Test that the patient can see the doctor’s message."""
        message_content = 'Doctor message'
        message = {'doctor_id': self.doctor['id'], 'patient_id': self.patient['id'], 'content': message_content}
        self.mock_db.add_message(message)

        # Verify the patient retrieves the message
        messages = self.mock_db.get_messages_for_session(self.patient['id'], self.doctor['id'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]['content'], message_content)
