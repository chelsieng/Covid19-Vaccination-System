from django.urls import path
from .views import *

urlpatterns = [
    path('<str:query>/', get_query),
    path('delete/<str:query>/', delete_record),
    path('edit/<str:query>/', edit_record)
]
