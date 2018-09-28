from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('catalog/', views.catalog),
    path('contacts/', views.contacts),
    path('<str:href>/', views.product_description, name='product_description'),
    # path('Asics_gel_pulse_9/', views.product_description),
    # path('asics_gel_solution_speed/', views.product_description),
    # path('Nike_flex_contact/', views.product_description),
]
