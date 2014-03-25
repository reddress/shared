from django.contrib import admin
from .models import Owner, AccountType, Account, Transaction
# Register your models here.

admin.site.register(Owner)
admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(Transaction)
