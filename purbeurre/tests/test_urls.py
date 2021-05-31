from django.test import SimpleTestCase
from django.urls import reverse, resolve
from purbeurre.views import product_info


class TestUrls(SimpleTestCase):

    def test_home_is_linked_to_good_url_and_views(self):
        self.assertEqual(reverse('home'), '/')
        self.assertEqual(resolve('/')._func_path, 'purbeurre.views.home')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! wrong page! Oups.')

    def test_legal_notices_is_linked_to_good_url_and_views(self):
        self.assertEqual(reverse('legal_notices'), '/mentions_legales')
        self.assertEqual(resolve('/mentions_legales')._func_path,
                         'purbeurre.views.legal_notices')

    def test_search_product_is_linked_to_good_url_and_views(self):
        self.assertEqual(reverse('search_product'), '/recherche')
        self.assertEqual(resolve('/recherche')._func_path,
                         'purbeurre.views.search_product')

    def test_product_info_url_resolves(self):
        url = reverse("product_info", args=['description'])
        self.assertEquals(resolve(url).func, product_info)
