from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a user with email is successfull"""
        email = "test@gl.com"
        password = '123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "gl@GL.COM"
        user = get_user_model().objects.create_user(email, 'test_133')
        self.assertEqual(user.email, email.lower())

    def test_invalid_new_user_email(self):
        """Test creating a user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "tet")

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'admin@test.com',
            'admin'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
