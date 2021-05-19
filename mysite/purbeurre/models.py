# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class CategoryProduct(models.Model):
	"""
	Class to create a table for the categories of products
	"""
	name_category = models.CharField(max_length=100)

	def __str__(self):
		return self.name_category


class ProductInfo(models.Model):
	"""
	Class to create a table for the products
	depending of their category (foreign key)
	"""
	name_product = models.CharField(max_length=200)
	category = models.ForeignKey(
		CategoryProduct, on_delete=models.CASCADE)
	nutrition_grade = models.CharField(default='none', max_length=1)
	image_product = models.URLField(default='None')
	url_product = models.URLField(default='None')
	image_nutrition = models.URLField(default='None')

	def __str__(self):
		return self.name_product


class UserSavingProduct(models.Model):
	"""
	Class to create a table to save the product
	(class Name) on the user account
	"""
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
