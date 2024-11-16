import unittest
from parameterized import parameterized, parameterized_class
from webapp.auth.forms import LoginForm, RegisterForm

class TestForms(unittest.TestCase):

    @parameterized.expand([
        ('test_user', 'test_password', True),
        ('invalid_user', 'test_password', False, 'Invalid username or password'),
        ('test_user', 'invalid_password', False, 'Invalid password')
    ])
    def test_login_form_validation(self, username, password,
                                   expected_result, error_message=None):
        form = LoginForm(username=username, password=password)
        self.assertEqual(form.validate(), expected_result)
        if not expected_result:
            self.assertIn(error_message, form.username.errors)

    @parameterized.expand([
        ('new_user', 'password123', 'password123', '1',
         'Cardiology', 'Cardiologist', 'test.jpg', True),
        ('new_user', 'password123', 'password123', '1', '', '', '', False,
         'Specialty and Bio and image is required for doctors'),
        ('new_user', 'password123', 'password123', '1', 'Cardiology',
         'Cardiologist', 'test.txt', False, 'Invalid image format'),
        ('existing_user', 'password123', 'password123', '1',
         'Cardiology', 'Cardiologist', 'test.jpg', False, 'User with that name already exists')
    ])
    def test_register_form_validation(self, username, password,
                                      confirm, role, specialty, bio,
                                      image, expected_result, error_message=None):
        form = RegisterForm(username=username,
                            password=password, confirm=confirm,
                            role=role, specialty=specialty,
                            bio=bio, image=image)
        self.assertEqual(form.validate(), expected_result)
        if not expected_result:
            self.assertIn(error_message, form.username.errors)

if __name__ == '__main__':
    unittest.main()