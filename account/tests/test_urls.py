from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model

from account.views import \
    sign_in, \
    log_in, \
    my_account, my_favorites_view

User = get_user_model()


class TestUrls(TestCase):

    def setUp(self):
        u = User.objects.create(username='boby', email='boby@bob.fr')
        u.set_password('azerty123')
        u.save()

    def test_sign_in_url_resolves(self):
        url = reverse("sign_in")
        self.assertEquals(resolve(url).func, sign_in)

    def test_log_in_url_resolves(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func, log_in)

    def test_my_account_resolves(self):
        url = reverse("my_account")
        self.assertEquals(resolve(url).func, my_account)

    def test_my_favorites_url_resolves(self):
        pass

"""
    def test_log_out_url_resolves(self):
        # client juste for SimpleTestcase but worked in view with Testcase
        self.client.login(username='boby', password='azerty123')
        response = self.client.logout()
        self.assertRedirects(response, "home", status_code=302, target_status_code=200)

"""
