from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('catalog.html/', views.catalog),
    path('contacts.html/', views.contacts),
    path('catalog/Adidas_Performance.html', views.adidas_performance),
    path('catalog/Asics_Gel_Pulse_9.html.html', views.asics_gel_pulse),
    path('catalog/asics_gel_solution_speed.html', views.asics_gel_solution_speed),
    path('catalog/Nike_Flex_Contact.html', views.nike_flex_contact),
]
