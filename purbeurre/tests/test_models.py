from django.test import TestCase

from purbeurre.models import CategoryProduct, ProductInfo, UserSavingProduct

"""
class BaseModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.category = CategoryProduct(name_category='pizzas')
        cls.category.save()

        cls.product = ProductInfo(category=cls.category, name_product='Pizza 4 stagioni')
        cls.product.save()


class TestCatProdModels(BaseModelTestCase):

    def test_category_created_properly(self):
        self.assertEqual(self.category.name_category, 'pizzas')
        self.assertEqual(True, self.category in self.product.objects.filter(category='pizzas'))

"""
""" 
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

    def test_user_saving_product_model(self):
        user_saving = UserSavingProduct(
            username='2',
            product=self.product_info.id
        )
        self.assertEqual(user_saving.product, self.product_info.id)
"""