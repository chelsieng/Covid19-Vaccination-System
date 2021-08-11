from django.urls import path
from .views import *

urlpatterns = [
    path('function/', function),
    path('<str:query>/', get_query)
]