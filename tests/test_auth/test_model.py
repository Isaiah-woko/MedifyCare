import unittest
from webapp.auth.models import User, Role

class TestUserAndRoleModels(unittest.TestCase):

    def setUp(self):
        # You can initialize any required objects or database connection here
        pass

    def test_user_has_role(self):
        user = User(username='test_user')
        role = Role(name='test_role')
        user.roles.append(role)
        self.assertTrue(user.has_role('test_role'))
        self.assertFalse(user.has_role('other_role'))

    def test_set_and_check_password(self):
        user = User(username='test_user')
        password = 'password123'
        user.set_password(password)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.check_password('wrong_password'))

    def test_user_authentication_properties(self):
        user = User(username='test_user')
        self.assertTrue(user.is_authenticated)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_anonymous)
        self.assertFalse(user.actived_subscription)  # Assuming correct property name

    def test_get_id_method(self):
        user = User(username='test_user')
        user.id = 1
        self.assertEqual(user.get_id(), '1')

    def test_activate_method(self):
        user = User(username='test_user')
        user.activate()
        self.assertTrue(user.activetion)

    def test_role_representation(self):
        role = Role(name='test_role')
        self.assertEqual(str(role), '<Role test_role>')

    def test_user_representation(self):
        user = User(username='test_user')
        self.assertEqual(str(user), '<User test_user>')
