from django.shortcuts import render
from .models import Currency


def display_prices(request):
    currencies = Currency.objects.all()
    return render(request, 'prices.html', {'currencies': currencies})
