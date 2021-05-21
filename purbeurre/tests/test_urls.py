from django.test import SimpleTestCase
from django.urls import reverse, resolve
from purbeurre.views import home, legal_notices, search_product, product_info


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, home)

    def test_legal_notices_url_resolves(self):
        url = reverse("legal_notices")
        self.assertEquals(resolve(url).func, legal_notices)

    def test_search_product_url_resolves(self):
        url = reverse("search_product")
        self.assertEquals(resolve(url).func, search_product)

    def test_product_info_url_resolves(self):
        url = reverse("product_info", args=['description'])
        self.assertEquals(resolve(url).func, product_info)
