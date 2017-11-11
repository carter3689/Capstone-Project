from django.contrib import admin

from .models import Transaction, TransactionSummary
# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'quantity','user', 'transaction_amount']
    search_fields = ['__str__']
    list_filter = ['price']
    # list_search = ['exhange']
    #list_editable=['']

    class Meta:
        model=Transaction


class TransactionSummaryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'symbol','symbol_total']
    search_fields = ['__str__']
    list_filter = ['symbol','user']
    # list_search = ['exhange']
    #list_editable=['']

    class Meta:
        model=TransactionSummary


admin.site.register(Transaction, TransactionAdmin, )
admin.site.register(TransactionSummary , TransactionSummaryAdmin, )
