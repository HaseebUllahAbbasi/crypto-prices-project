from django.shortcuts import render
from .models import CryptoPrice, Currency


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
    generate_static_data()

    # Fetch all currencies including the static ones
    latest_crypto_price = CryptoPrice.objects.latest('timestamp')

    # Get currencies associated with the latest CryptoPrice entry
    currencies = Currency.objects.filter(crypto_prices=latest_crypto_price)

    # Prepare context to pass to the template
    context = {
        'latest_crypto_price': latest_crypto_price,
        'currencies': currencies
    }
    return render(request, 'prices.html', {'currencies': currencies})
