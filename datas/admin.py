from django.contrib import admin
from .models import Deposit, DepositProduct, CIF, Financing, Collateral


# Register your models here.

admin.site.register(Deposit)
admin.site.register(DepositProduct)
admin.site.register(CIF)
admin.site.register(Financing)
admin.site.register(Collateral)