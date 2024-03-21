from django.shortcuts import render
from .models import CryptoPrice, Currency
import requests


def generate_static_data():
    # Create a CryptoPrice object to associate with static currencies
    crypto_price = CryptoPrice.objects.create()

    # Define static data for currencies
    static_currencies = [
        {'name': 'BTC', 'value': 50000},
        {'name': 'ETH', 'value': 3000},
        {'name': 'SOL', 'value': 150},
    ]

    # Save static data into the Currency model
    for currency_data in static_currencies:
        Currency.objects.create(
            crypto_prices=crypto_price,
            name=currency_data['name'],
            value=currency_data['value']
        )


def display_prices(request):
    # Generate and save static data
    # generate_static_data()

    # Fetch all currencies including the static ones
    last_updated = CryptoPrice.objects.latest('timestamp')

    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,solana,ethereum&vs_currencies=usd')
    data = response.json()

    # Get currencies associated with the latest CryptoPrice entry
    currencies = Currency.objects.filter(crypto_prices=last_updated)

    # Prepare context to pass to the template

    return render(request, 'prices.html', {'last_updated': last_updated,
                                           'currencies': currencies, 'data': data})
