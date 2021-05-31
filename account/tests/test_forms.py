from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCast(TestCase):

    def setUp(self):
        self.user_a = User(username='cfe', email='cfe@invalid.com')
        self.user_a.name = True
        self.user_a.is_superuser = True
        self.user_a.set_password('itsapassword1')
        self.user_a.save()

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

    def test_new_user_added_is_created(self):
        self.assertEqual(len(User.objects.filter(username="bobby")), 0)

        bobby = User(username="Bobby", email="bobby@test.com")
        bobby.save()

        return_user = User.objects.filter(username="Bobby")
        self.assertEqual(len(return_user), 1)
        self.assertEqual(return_user[0].username, bobby.username)
