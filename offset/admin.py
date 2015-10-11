from django.contrib import admin
from offset.models import Transaction
from offset.models import Mortgage
from offset.models import Order

admin.site.register(Transaction)
admin.site.register(Mortgage)
admin.site.register(Order)