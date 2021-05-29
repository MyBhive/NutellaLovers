from django.test import TestCase, Client
from django.urls import reverse
from purbeurre.models import CategoryProduct, ProductInfo


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.legal_notices_url = reverse('legal_notices')
        self.search_product_url = reverse('search_product')
        self.product_info_url = reverse('product_info', args=["159"])
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

    def test_home_view(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_legal_notices_view(self):
        response = self.client.get(self.legal_notices_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/mentions_legales.html')

    def test_search_product_in_database(self):
        research_user = 'nutella'
        result = ProductInfo.objects.filter(
            name_product__contains=research_user
        )[0]
        self.assertEquals(research_user, result.name_product)

    def test_find_substitute_in_database(self):
        research_user = 'nutella'
        result = ProductInfo.objects.filter(
            name_product__contains=research_user
        )[0]
        products = ProductInfo.objects.filter(
            category=result.category,
            nutrition_grade__lt=result.nutrition_grade) \
            .order_by("nutrition_grade")[0]
        self.assertEqual(products.name_product, 'Duo')

    def test_search_product_not_find(self):
        pass #message d'erreur écrit en html

    def test_render_product_informations(self):
        #ne marche pas
        response = self.client.get('search_product')
        prod = ProductInfo.objects.get(id=self.prod_info.id)


