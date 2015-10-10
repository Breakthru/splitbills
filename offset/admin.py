from django.contrib import admin
from offset.models import Transaction
from offset.models import Mortgage

admin.site.register(Transaction)
admin.site.register(Mortgage)