# coding: utf-8
from django.urls import path

from . import views

"""Path to connect views to the frontend"""

urlpatterns = [
    path('', views.home, name='home'),
    path('mentions_legales', views.legal_notices, name='legal_notices'),
    path('recherche', views.search_product, name='search_product'),
    path("infos_produit/<str:description>/",
         views.product_info,
         name="product_info")
]
