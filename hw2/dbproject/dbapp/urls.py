from django.urls import path
from .views import client_ordered_products

urlpatterns = [
    path('client/<int:client_id>/ordered_products/<int:days>/', client_ordered_products, name='client_ordered_products'),
]

