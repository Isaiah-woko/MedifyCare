import unittest
from webapp import create_app, db
from webapp.auth.models import User
import os
from flask import url_for
class TestAppSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create app with testing configuration
        env = os.environ.get('WEBAPP_ENV', 'dev') ## if is not in environment just return dev
        cls.app = create_app('config.%sConfig' % env.capitalize())
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Clean up database and application context
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def setUp(self):
        # Set up a test client for each test
        self.client = self.app.test_client()
        self.init_database()

    def tearDown(self):
        # Clean up the database after each test
        db.session.query(User).delete()
        db.session.commit()

    # create a user
    def init_database(self):
        # Add a sample user to the database
        user = User(username="testuser", email="test@gmail.com")
        user.set_password("password123")
        db.session.add(user)
        db.session.commit()

    # retrieve the user
    def test_user_creation(self):
        # Test if the sample user is in the database
        user = User.query.filter_by(username="testuser").first()
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testuser")

    # login
    def test_user_login_valid(self):
        # Simulate a login request
        response = self.client.post(
            '/auth/login',
            data={'username': 'testuser', 'password': 'password123'}
        )
        self.assertEqual(response.status_code, 200)
        # Check if the redirection is to the 'main.index' route
        with self.app.test_request_context():
            self.assertIn(url_for('main.index'), response.request.path)

    # Test Case: User Login (Invalid Credentials)
    def test_user_login_invalid(self):
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'wrongpassword'
        }, follow_redirects=True)
        assert response.status_code == 200
        self.assertIn(b'Invalid password', response.data)

    
    # # Test Case: Login Required to Access Protected Route
    # def test_protected_route_requires_login(client):
    #     response = client.get('/protected-route')  # Replace with an actual protected route
    #     assert response.status_code == 302  # Redirect to login page
    #     assert b'login' in response.headers['Location']

    # # Test Case: User Logout
    # def test_user_logout(client, init_database):
    #     # Log in first
    #     client.post('/login', data={
    #         'email': 'testuser@example.com',
    #         'password': 'password123'
    #     }, follow_redirects=True)
