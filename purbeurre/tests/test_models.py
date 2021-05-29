from django.test import TestCase

from purbeurre.models import CategoryProduct, ProductInfo, UserSavingProduct


class TestModels(TestCase):
    def setUp(self):
        pass

    def test_category_product_model(self):
        self.category = CategoryProduct(
            name_category="pizzas"
        )
        self.assertEqual(str(self.category), self.category.name_category)

    def test_product_model(self):
        self.product_info = ProductInfo(
            name_product='Pizza 4 stagioni',
        )
        self.assertEquals(str(self.product_info), self.product_info.name_product)

"""
    def test_user_saving_product_model(self):
        user_saving = UserSavingProduct(
            username='2',
            product=self.product_info.id
        )
        self.assertEqual(user_saving.product, self.product_info.id)
"""