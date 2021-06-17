from django.contrib.auth import get_user_model
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

from purbeurre.models import ProductInfo, CategoryProduct

User = get_user_model()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument('--headless')


class TestSeleniumUserPath(StaticLiveServerTestCase):
    def setUp(self):
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

    def test_user_journey(self):
        # sign_in
        driver = webdriver.Chrome('account/tests/chromedriver.exe')
        driver.implicitly_wait(30)
        driver.get('%s%s' % (self.live_server_url, '/sign_in/'))
        self.assertEqual(len(User.objects.all()), 0)
        driver.find_element_by_name('username').send_keys('selenium')
        driver.find_element_by_name('email').send_keys('selenium@gmail.com')
        driver.find_element_by_name('password1').send_keys('champignon1')
        driver.find_element_by_name('password2').send_keys('champignon1')
        driver.find_element_by_id('valid_sign_in').click()
        self.assertEqual(driver.title, 'Log in')
        self.assertEqual(len(User.objects.all()), 1)
        # log in
        driver.find_element_by_name('username').send_keys('selenium')
        driver.find_element_by_name('password').send_keys('champignon1')
        driver.find_element_by_id('valid_log_in').click()
        user_log = User.objects.get(username='selenium')
        self.assertTrue(user_log.check_password('champignon1'))
        driver.get('%s%s' % (self.live_server_url, '/'))
        self.assertEqual(driver.title, 'Pur Beurre')
        # search product
        driver.find_element_by_name('user_research').send_keys('nutella')
        driver.find_element_by_name('research').click()
        self.assertEqual(driver.title, 'Recherche')
        driver.find_element_by_name('save').click()
        time.sleep(5)
        driver.quit()
