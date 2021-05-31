from django.test import TestCase

from purbeurre.models import CategoryProduct, ProductInfo


class TestCatProdModels(TestCase):
    def setUp(self):
        self.category = CategoryProduct(
            name_category='pates-a-tartiner')
        self.category.save()

        self.prod_info = ProductInfo.objects.create(
            name_product="nutella",
            category=self.category,
            nutrition_grade="e",
            image_product="www.image-nutellat.com",
            url_product="www.nutella.com",
            image_nutrition="www.img_nutri.com"
        )
        self.prod_info.save()

    def test_category_created_properly(self):
        self.assertEqual(self.category.name_category,
                         'pates-a-tartiner')

    def test_product_created_properly(self):
        self.assertEquals(str(self.prod_info), 'nutella')
