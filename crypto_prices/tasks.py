# tasks.py
import logging
from .models import Currency
from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def update_prices():
    # Log before making API call
    logger.info("Before API call")

    # response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,solana,ethereum&vs_currencies=usd')
    # data = response.json()

    # Example static data (for testing purposes)
    static_data = {
        "bitcoin": {"usd": 45000},
        "solana": {"usd": 150},
        "ethereum": {"usd": 3000}
    }

    # Log API response data (or static data for testing)
    logger.info("API response data: %s", static_data)

    # Update database with static data
    for name, value in static_data.items():
        currency, created = Currency.objects.get_or_create(
            name=name, defaults={'value': value['usd']})
        if not created:
            # If currency already exists, update its value
            currency.value = value['usd']
            currency.save()

    # Log after updating database
    logger.info("Database updated successfully")
