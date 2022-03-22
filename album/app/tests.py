from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import App
from django.test import SimpleTestCase


class CustomUserTests(TestCase):


    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
        username='will',
        email='will@email.com',
        password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)



# class SimpleTests(SimpleTestCase):
#
#     def test_home_page_status_code(self):
#         response = self.client.get('/api/v1/')
#         self.assertEqual(response.status_code, 200)

    # def test_about_page_status_code(self):
    #     response = self.client.get('/v1/post/')
    #     self.assertEqual(response.status_code, 200)