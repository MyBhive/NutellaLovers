from django.test import TestCase, Client
from purbeurre.models import UserSavingProduct, ProductInfo, CategoryProduct
from account.forms import SignInForm
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class RegisterViewTestCase(TestCase):

    def setUp(self):
        user = User(username='cfe', email='cfe@invalid.com')
        user.name = True
        user.is_superuser = True
        user.set_password('itsapassword1')
        user.save()

    def test_sign_in_success(self):
        response = self.client.post('/sign_in/',
                                    {'username': 'nico2',
                                     'email': "nico2@gmail.com",
                                     'password1': '123nousironsaubois!',
                                     'password2': '123nousironsaubois!'})

        self.assertEquals(response.status_code, 302)

    def test_sign_in_username_already_exist(self):
        pass

"""
    def test_sign_in_error_password(self):
        response = self.client.post('/sign_in/',
                                    {'username': 'bob',
                                     'email': 'bob@cfe.com',
                                     'password1': '123nousironsaubois!',
                                     'password2': '007nousironsaubois!'})
        self.assertContains(response, ))
"""


class LoginViewTestCase(TestCase):

    def setUp(self):
        u = User.objects.create(username='boby', email='boby@bob.fr')
        u.set_password('azerty123')
        u.save()

    def test_login_success(self):
        response = self.client.login(username='boby',
                                     password='azerty123')
        self.assertTrue(response)

    def test_login_password_wrong(self):
        pass

    def log_out_redirect(self):
        pass

"""
class SaveAndViewTestCaseOfFavorite(TestCase):

    def setUp(self):
        user_a = User(username='cfe', email='cfe@invalid.com')
        user_a.set_password('itsapassword1')
        user_a.save()
        self.user_id = '2'
        self.client = Client()
        self.home_url = reverse('home')
        self.category = CategoryProduct.objects.create(
            name_category="pates-a-tartiner"
        )
        self.prod_info = ProductInfo.objects.create(
            name_product="nutella",
            category=self.category,
            nutrition_grade="e",
            image_product="www.image-nutellat.com",
            url_product="www.nutella.com",
            image_nutrition="www.img_nutri.com"
        )

        self.substitute = ProductInfo.objects.create(
            name_product="Duo",
            category=self.category,
            nutrition_grade="b",
            image_product="www.image-duo.com",
            url_product="www.duo.com",
            image_nutrition="www.img_nutri.com"
        )

        self.user_login = UserSavingProduct.objects.create(
            username=User(username='bobby'),
            product=self.substitute
        )

    def test_save_favorite_success(self):
        pass

    def test_my_favorite_view(self):
        pass


    def test_saving_favorite_fails_product_already_exist(self):
        research_user = 'duo'
        result = UserSavingProduct.objects.get(
            username_id=self.user_id, product_id=research_user.id)
        self.assertContains(self.user_login, result)
"""



