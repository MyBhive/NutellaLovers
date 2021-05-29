from django.test import LiveServerTestCase
from selenium import webdriver
import time


class TestForm(LiveServerTestCase):

    def test_form_sign_in(self):
        driver = webdriver.Chrome('account/tests/chromedriver.exe')
        driver.implicitly_wait(30)
        driver.get('%s%s' % (self.live_server_url, '/sign_in/'))
        username = driver.find_element_by_name('username')
        email = driver.find_element_by_name('email')
        password1 = driver.find_element_by_name('password1')
        password2 = driver.find_element_by_name('password2')
        submit = driver.find_element_by_id('valid_sign_in')
        # fill in the form with data
        username.send_keys('selenium')
        email.send_keys('selenium@gmail.com')
        password1.send_keys('champignon1')
        password2.send_keys('champignon1')
        # submit form
        submit.click()
        time.sleep(1)
        driver.quit()

    def test_form_log_in(self):
        driver = webdriver.Chrome('account/tests/chromedriver.exe')
        driver.implicitly_wait(30)
        driver.get('%s%s' % (self.live_server_url, '/login/'))
        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')

        username.send_keys('selenium@gmail.com')
        password.send_keys('champignon1')
        submit = driver.find_element_by_id('valid_log_in')
        submit.click()
        time.sleep(1)
        driver.quit()

    def test_research_product(self):
        driver = webdriver.Chrome('account/tests/chromedriver.exe')
        driver.implicitly_wait(30)
        driver.get('%s%s' % (self.live_server_url, '/'))
        research = driver.find_element_by_name('user_research')
        research.send_keys('potiron')
        submit = driver.find_element_by_name('research')
        submit.click()
        time.sleep(1)
        driver.quit()

"""
    def test_add_product_to_favorite(self):
        driver = webdriver.Chrome('account/tests/chromedriver.exe')
        driver.implicitly_wait(30)
        driver.get('%s%s' % (self.live_server_url, '/recherche?user_research=potiron'))
        submit = driver.find_element_by_name('save')
        submit.click()
        time.sleep(1)
        driver.quit()
        dois-je créer un db fictiv comme pour les tests unitaire?
        shell
      from purbeurre.models import ProductInfo
>>> research_user = request.GET.get('potiron')
>>> result = ProductInfo.objects.filter(name_product__contains='potiron')[0]
>>> products = ProductInfo.objects.filter(category=result.category,nutrition_grade__lt=result.nutrition_grade).order_by('nutrition_grade')[:6]
>>> print(result)
velouté de potiron et châtaigne
>>> print(products)
<QuerySet [<ProductInfo: Knorr Comme à La Maison Soupe Liquide Légumes du Potager 45cl>, <ProductInfo: Gazpacho original sin gluten envase 1 l>, <ProductInfo: Soupe froide tomate, menthe & basilic>, <ProductInfo: Knorr Comme à La Maiso
n Soupe Liquide Patate Douce Carottes Fromage Frais Bouteille de>, <ProductInfo: velouté de tomates>, <ProductInfo: Gazpacho>]>
>>>      
"""