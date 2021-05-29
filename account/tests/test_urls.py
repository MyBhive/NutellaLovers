from django.test import SimpleTestCase
from django.urls import reverse, resolve

from account.views import \
    sign_in, \
    log_in, \
    my_account, my_favorites_view


class TestUrls(SimpleTestCase):

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

    def test_log_out_url_resolves(self):
        pass


