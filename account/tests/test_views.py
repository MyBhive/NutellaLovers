from django.test import TestCase, RequestFactory, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from purbeurre.models import UserSavingProduct, ProductInfo, CategoryProduct
from account.views import save_in_favorite

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
        self.assertEqual(len(User.objects.filter(username='nico2')), 1)

    def test_sign_in_username_already_exist(self):
        response = self.client.post('/sign_in/',
                                    {'username': 'cfe',
                                     'email': "nico2@gmail.com",
                                     'password1': '123nousironsaubois!',
                                     'password2': '123nousironsaubois!'})
        self.assertEqual(response.context['form'].errors['username'][0],
                         'Un utilisateur avec ce nom existe déjà.')
        self.assertEqual(response.status_code, 200)

    def test_sign_in_error_password(self):
        response = self.client.post('/sign_in/',
                                    {'username': 'bob',
                                     'email': 'bob@cfe.com',
                                     'password1': '123nousironsaubois!',
                                     'password2': '007nousironsaubois!'})
        self.assertEqual(response.context['form'].errors['password2'][0],
                         'Les deux mots de passe ne correspondent pas.')


class LoginViewTestCase(TestCase):

    def setUp(self):
        self.u = User.objects.create(username='boby', email='boby@bob.fr')
        self.u.set_password('azerty123')
        self.u.save()

    def test_login_success(self):
        self.assertEqual(self.client.session.get(
            '_auth_user_id', False),
            False
        )
        self.client.post('/login/',
                         {'username': 'boby',
                          'password': 'azerty123'})
        self.assertEqual(self.client.session['_auth_user_id'],
                         str(self.u.pk
                             ))

    def test_login_password_wrong(self):
        self.assertEqual(self.client.session.get(
            '_auth_user_id', False),
            False
        )
        response = self.client.post('/login/',
                                    {'username': 'boby',
                                     'password': 'azerty123!'}
                                    )
        self.assertContains(response,
                            'Identifiant ou mot de passe incorrect'
                            )
        self.assertEqual(self.client.session.get(
            '_auth_user_id', False),
            False
        )

    def test_log_out_redirect(self):
        self.client.login(username='boby', password='azerty123')
        self.assertEqual(self.client.session.get(
            '_auth_user_id', False),
            str(self.u.pk)
        )
        response = self.client.get('/log_out/', follow=True)
        self.assertEqual(self.client.session.get(
            '_auth_user_id', False),
            False
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertTemplateUsed(response, 'pages/head_foot_nav.html')

    def test_my_account_view_success(self):
        response = self.client.get(reverse('my_account'))
        self.assertEquals(response.status_code, 302)


class SaveAndViewTestCaseOfFavorite(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.u = User.objects.create(username='bob',
                                     email='bob@fake.fr')
        self.u.set_password('azerty123')
        self.u.save()
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

    def test_save_favorite_success(self):
        request = self.factory.get('recherche')
        request.user = self.u
        pre_number_product = len(UserSavingProduct.objects.filter(
            product=self.substitute.id))
        self.assertEqual(pre_number_product, 0)
        save_in_favorite(request, self.substitute.id)
        self.assertEqual(pre_number_product + 1, 1)

    def test_my_favorite_view(self):
        response = self.client.get(reverse('my_favorites_view'))
        self.assertEquals(response.status_code, 302)


