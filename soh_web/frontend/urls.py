
from django.contrib import admin
from django.urls import path
from frontend.views import main_app
from frontend.views import partner_detail

urlpatterns = [
    path('', main_app),
    path('partner/<str:partner_title>/', partner_detail, name='partner_detail'),
]
