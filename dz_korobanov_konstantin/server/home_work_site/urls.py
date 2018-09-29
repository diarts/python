from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('catalog/', views.catalog),
    path('contacts/', views.contacts),
    path('<str:name>/', views.product_description, name='product_description'),
]
