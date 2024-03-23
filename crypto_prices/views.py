from django.shortcuts import render
from .models import CryptoPrice, Currency
import requests


def generate_dynamic_data():
    crypto_price = CryptoPrice.objects.create()
    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,solana,ethereum&vs_currencies=usd')
    data = response.json()

    for currency_name, currency_data in data.items():
        Currency.objects.create(
            crypto_prices=crypto_price,
            name=currency_name,
            value=currency_data['usd']
        )


def display_prices(request):
    last_updated = CryptoPrice.objects.latest('timestamp')
    currencies = Currency.objects.filter(crypto_prices=last_updated)
    print(last_updated)
    return render(request, 'prices.html', {'last_updated': last_updated,
                                           'currencies': currencies, })
