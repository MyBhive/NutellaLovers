from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCast(TestCase):

    def setUp(self):
        user_a = User(username='cfe', email='cfe@invalid.com')
        user_a.name = True
        user_a.is_superuser = True
        user_a.set_password('itsapassword1')
        user_a.save()

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
