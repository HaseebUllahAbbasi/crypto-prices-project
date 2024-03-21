from django.db import models


class CryptoPrice(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Timestamp: {self.timestamp}"


class Currency(models.Model):
    crypto_prices = models.ForeignKey(CryptoPrice, on_delete=models.CASCADE)
    name = models.CharField(max_length=4)
    value = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return f"{self.name}: {self.value}"
