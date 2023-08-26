from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('test/', test_api),
    path('<int:id>/', random_quiz),
]
