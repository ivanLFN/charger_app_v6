
from django.contrib import admin
from django.urls import path
from frontend.views import main_app

urlpatterns = [
    path('', main_app)
]
