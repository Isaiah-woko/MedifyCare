import unittest
from unittest.mock import MagicMock
from webapp import create_app, db
from webapp.auth.models import User
from webapp.chat.models import Message
from flask import jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit
import os

class MockDatabase(unittest.TestCase):
    """
    A mock database to simulate chat messages between doctors and patients
    """
    def __init__(self):
        self.messages = []  # Stores mock chat messages
        self.users = []  # Stores mock users (doctor, patient)

    def add_message(self, message):
        self.messages.append(message)

    def get_messages_for_session(self, doctor_id, patient_id):
        """Get messages between a doctor and a patient."""
        return [msg for msg in self.messages if (msg['doctor_id'] == doctor_id and msg['patient_id'] == patient_id) or 
                (msg['doctor_id'] == patient_id and msg['patient_id'] == doctor_id)]


class ChatTestCase(unittest.TestCase):
    """
    Test cases for the chat functionality
    """

    @classmethod
    def setUpClass(cls):
        """Set up the Flask application and mock database."""
        env = os.environ.get('WEBAPP_ENV', 'dev') ## if is not in environment just return dev
        cls.app = create_app('config.%sConfig' % env.capitalize())
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        
        # Initialize the mock database
        cls.mock_db = MockDatabase()

        # Mock users (doctor and patient)
        cls.doctor = {'id': 1, 'username': 'doctor'}
        cls.patient = {'id': 2, 'username': 'patient'}
        cls.mock_db.users.extend([cls.doctor, cls.patient])

    @classmethod
    def tearDownClass(cls):
        """Clean up after the tests."""
        cls.app_context.pop()

    def test_doctor_can_send_message(self):
        """Test that a doctor can send a message to a patient."""
        # Simulate sending a message from the doctor to the patient
        message_content = 'Hello, Patient!'
        message = {'doctor_id': self.doctor['id'], 'patient_id': self.patient['id'], 'content': message_content}
        self.mock_db.add_message(message)

        # Verify the message is saved in the mock database
        messages = self.mock_db.get_messages_for_session(self.doctor['id'], self.patient['id'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]['content'], message_content)

    def test_patient_can_send_message(self):
        """Test that a patient can send a message to a doctor."""
        # Simulate sending a message from the patient to the doctor
        message_content = 'Hello, Doctor!'
        message = {'doctor_id': self.doctor['id'], 'patient_id': self.patient['id'], 'content': message_content}
        self.mock_db.add_message(message)

        # Verify the message is saved in the mock database
        messages = self.mock_db.get_messages_for_session(self.doctor['id'], self.patient['id'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]['content'], message_content)

    def test_doctor_can_see_patient_message(self):
        """Test that the doctor can see the patient’s message."""
        # Simulate sending a message from the patient to the doctor
        message_content = 'Patient message'
        message = {'doctor_id': self.doctor['id'], 'patient_id': self.patient['id'], 'content': message_content}
        self.mock_db.add_message(message)

        # Simulate the doctor retrieving messages
        messages = self.mock_db.get_messages_for_session(self.doctor['id'], self.patient['id'])

        # Verify the message order is correct
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]['content'], message_content)

    def test_patient_can_see_doctor_message(self):
        """Test that the patient can see the doctor’s message."""
        # Simulate sending a message from the doctor to the patient
        message_content = 'Doctor message'
        message = {'doctor_id': self.doctor['id'], 'patient_id': self.patient['id'], 'content': message_content}
        self.mock_db.add_message(message)

        # Simulate the patient retrieving messages
        messages = self.mock_db.get_messages_for_session(self.patient['id'], self.doctor['id'])

        # Verify the message order is correct
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]['content'], message_content)