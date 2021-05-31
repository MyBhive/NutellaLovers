from django.test import TestCase, Client
from django.urls import reverse

from purbeurre.models import CategoryProduct, ProductInfo


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.legal_notices_url = reverse('legal_notices')
        self.category = CategoryProduct.objects.create(
            name_category="pates-a-tartiner"
        )
        self.substitute = ProductInfo.objects.create(
            name_product="Duo",
            category=self.category,
            nutrition_grade="b",
            image_product="www.image-duo.com",
            url_product="www.duo.com",
            image_nutrition="www.img_nutri.com"
        )

        self.prod_info = ProductInfo.objects.create(
            name_product="nutella",
            category=self.category,
            nutrition_grade="e",
            image_product="www.image-nutellat.com",
            url_product="www.nutella.com",
            image_nutrition="www.img_nutri.com"
        )

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertTemplateUsed(response, 'pages/head_foot_nav.html')

    def test_legal_notices_view(self):
        response = self.client.get(self.legal_notices_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/mentions_legales.html')

    def test_search_product_not_find(self):
        research = "cacahuète"
        response = self.client.get('/recherche',
                                   data={'user_research': research})
        self.assertContains(response,
                            text='Produit introuvale.'
                                 ' Merci de relancer une recherche')

    def test_find_substitute_in_database(self):
        research = "nutella"
        response = self.client.get('/recherche',
                                   data={'user_research': research})
        better_product = response.context['products']
        self.assertEqual(list(better_product),
                         [self.substitute])

    def test_product_informations_render_correctly(self):
        response = self.client.get(f'/infos_produit/{self.substitute.id}/')
        self.assertContains(response, "Duo")

    def test_view_detail_product_return_response_200_if_product_exists(self):
        response = self.client.get(f'/infos_produit/{self.substitute.id}/')
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(response.status_code, 200)
