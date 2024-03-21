# tasks.py
import logging
import requests
from .models import Currency
from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def update_prices():
    logger.debug("Fetching cryptocurrency prices from Coingecko API...")
    # Fetch prices from Coingecko API
    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,solana,ethereum&vs_currencies=usd')
    data = response.json()

    logger.debug("Received data from Coingecko API: %s", data)

    # Store data in database
    for name, value in data.items():
        currency_name = name.capitalize()  # Capitalize the currency name
        currency_value = value['usd']

        # Check if currency exists in database, update if exists, create if not
        currency, created = Currency.objects.update_or_create(
            name=currency_name,
            defaults={'value': currency_value}
        )

        logger.debug("Stored %s price in database: $%s",
                     currency_name, currency_value)

# import logging
# from .models import Currency
# from celery import shared_task

# logger = logging.getLogger(__name__)


# @shared_task
# def update_prices():
#     # Log before making API call
#     logger.info("Before API call")

#     # response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,solana,ethereum&vs_currencies=usd')
#     # data = response.json()

#     # Example static data (for testing purposes)
#     static_data = {
#         "bitcoin": {"usd": 45000},
#         "solana": {"usd": 150},
#         "ethereum": {"usd": 3000}
#     }

#     # Log API response data (or static data for testing)
#     logger.info("API response data: %s", static_data)

#     # Update database with static data
#     for name, value in static_data.items():
#         currency, created = Currency.objects.get_or_create(
#             name=name, defaults={'value': value['usd']})
#         if not created:
#             # If currency already exists, update its value
#             currency.value = value['usd']
#             currency.save()

#     # Log after updating database
#     logger.info("Database updated successfully")
