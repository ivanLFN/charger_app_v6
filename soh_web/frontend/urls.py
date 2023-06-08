
from django.contrib import admin
from django.urls import path
from frontend.views import main_app
from frontend.views import partner_detail, store, product_detail, personal_data


urlpatterns = [
    path('', main_app),
    path('partner/<str:partner_title>/', partner_detail, name='partner_detail'),
    path('store/', store, name='store'),
    path('store/<str:product_title>/', product_detail, name='product_detail'),
    path('personal_data/', personal_data, name='personal_data')
]
