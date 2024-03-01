from django.shortcuts import render

# Create your views here.


# views.py

from django.shortcuts import render
from .models import Client, Order, Product
from django.utils import timezone
from datetime import timedelta

def client_ordered_products(request, client_id, days):
    client = Client.objects.get(pk=client_id)
    end_date = timezone.now()
    start_date = end_date - timedelta(days=days)
    ordered_products = Product.objects.filter(order__client=client, order__order_date__range=(start_date, end_date)).distinct()

    context = {
        'client': client,
        'ordered_products': ordered_products,
        'days': days,
    }

    return render(request, 'client_ordered_products.html', context)
