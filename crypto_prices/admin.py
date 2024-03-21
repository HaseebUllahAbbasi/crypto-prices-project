# admin.py
from django.contrib import admin
from .models import CryptoPrice, Currency

# Register your models here.
admin.site.register(CryptoPrice)
admin.site.register(Currency)
