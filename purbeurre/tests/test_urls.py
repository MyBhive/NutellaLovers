from django.test import SimpleTestCase
from django.urls import reverse, resolve
from purbeurre.views import home, legal_notices, search_product, product_info


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, home)

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! wrong page! Oups.')

    def test_legal_notices_url_resolves(self):
        url = reverse("legal_notices")
        self.assertEquals(resolve(url).func, legal_notices)

    def test_search_product_url_resolves(self):
        url = reverse("search_product")
        self.assertEquals(resolve(url).func, search_product)

    def test_product_info_url_resolves(self):
        url = reverse("product_info", args=['description'])
        self.assertEquals(resolve(url).func, product_info)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html', 'pages/head_foot_nav.html')
