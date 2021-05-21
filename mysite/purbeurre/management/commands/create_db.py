# coding: utf-8
import requests

from django.core.management.base import BaseCommand
from django.db.utils import DataError, IntegrityError

from mysite.purbeurre.models import ProductInfo, CategoryProduct


class Command(BaseCommand):
	"""
	This class handle the informations from OFF API.
	CATEGORIES: Constant data for the purbeurre application
	"""
	CATEGORIES = [
		"pates-a-tartiner",
		"Biscuits",
		"Pizzas",
		"chocolats",
		"boissons-gazeuses",
		"pains",
		"yaourts",
		"viandes",
		"soupes",
		"glace"
	]

	def insert_data(self):
		"""
		Method to :
		- insert the categories from CONSTANT CATEGORY
		inside the category table
		- take from openfoodfacts API the product
		- insert a certain amount of product inside the product table
		depending of the category they
		"""
	for category in CATEGORIES:
		category_name = CategoryProduct.objects.get_or_create(name_category=category)

		url = "https://fr.openfoodfacts.org/cgi/search.pl"
		payload = {
			"action": "process",
			"tagtype_0": "categories",
			"tag_contains_0": "contains",
			"tag_0": category,
			"sort_by": "unique_scans_n",
			"page_size": "300",
			"json": "1"}

		response = requests.get(url, params=payload)
		package = response.json()
		prod_base = package['products']

		for product in prod_base:
			try:
				name_product = product['product_name']
				nutrition_grade = product['nutrition_grades']
				image_product = product['image_front_url']
				url_product = product['url']
				image_nutrition = product['image_nutrition_small_url']

				ProductInfo.objects.get_or_create(
					name_product=name_product,
					category=category_name[0],
					nutrition_grade=nutrition_grade,
					image_product=image_product,
					url_product=url_product,
					image_nutrition=image_nutrition
					)

			except KeyError:
				pass

			except DataError:
				pass

			except IntegrityError:
				pass

	def handle(self, *args, **options):
		self.insert_data()
