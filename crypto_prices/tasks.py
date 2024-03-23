# tasks.py
import logging
import requests
from .models import Currency
from celery import shared_task
from .models import CryptoPrice, Currency


logger = logging.getLogger(__name__)


@shared_task
def update_price_list():
    logger.debug("Fetching cryptocurrency prices from Coingecko API...")
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
    logger.debug("Stored cryptocurrency prices from Coingecko API...")
