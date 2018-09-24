from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('catalog/', views.catalog),
    path('contacts/', views.contacts),
    path('Adidas_Performance/', views.product_description),
    path('Asics_Gel_Pulse_9/', views.product_description),
    path('asics_gel_solution_speed/', views.product_description),
    path('Nike_Flex_Contact/', views.product_description),
]
