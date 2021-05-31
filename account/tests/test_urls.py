from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model


User = get_user_model()


class TestUrls(TestCase):

    def setUp(self):
        u = User.objects.create(
            username='boby',
            email='boby@bob.fr'
        )
        u.set_password('azerty123')
        u.save()

    def test_login_url_is_linked_to_good_url(self):
        self.assertEqual(reverse('login'), '/login/')
        self.assertEqual(resolve('/login/')._func_path,
                         'account.views.log_in'
                         )

    def test_sign_in_url_is_linked_to_good_url(self):
        self.assertEqual(reverse('sign_in'), '/sign_in/')
        self.assertEqual(resolve('/sign_in/')._func_path,
                         'account.views.sign_in'
                         )

    def test_logout_url_is_linked_to_good_url(self):
        self.assertEqual(reverse('log_out'), '/log_out/')
        self.assertEqual(resolve('/log_out/')._func_path,
                         'account.views.log_out'
                         )

    def test_my_account_is_linked_to_good_url(self):
        self.assertEqual(reverse('my_account'), '/mon_compte/')
        self.assertEqual(resolve('/mon_compte/')._func_path,
                         'account.views.my_account'
                         )

    def test_my_favorites_is_linked_to_good_url(self):
        self.assertEqual(reverse('save_in_favorite',
                                 args=[1]),
                         '/mes_favoris/1/'
                         )
        self.assertEqual(resolve('/mes_favoris')._func_path,
                         'account.views.my_favorites_view'
                         )

    def test_my_favorites_products_is_linked_to_good_url(self):
        self.assertEqual(reverse('my_favorites_view'), '/mes_favoris')
        self.assertEqual(resolve('/mes_favoris')._func_path,
                         'account.views.my_favorites_view'
                         )
