from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mentions_legales', views.legal_notices, name='legal_notices'),
    path('recherche', views.search_product, name='search_product'),
    path('substitut', views.search_substitute, name='search_substitute'),
    path("infos_produit", views.product_info, name="product_info")
]
