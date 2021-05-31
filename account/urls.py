# coding: utf-8
from django.urls import path

from . import views

"""Path to connect views to the frontend"""

urlpatterns = [
    path('login/', views.log_in, name="login"),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('mon_compte/', views.my_account, name='my_account'),
    path('mes_favoris/<str:product_id>/',
         views.save_in_favorite,
         name='save_in_favorite'),
    path('mes_favoris', views.my_favorites_view,
         name="my_favorites_view")
]
