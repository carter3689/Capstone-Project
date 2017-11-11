from django.db import models

# Create your models here.
from instruments.models import Instrument,Variation
from django.conf import settings
from django.db.models import Sum

class Transaction(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, null =True, blank = True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits = 50,decimal_places = 3,blank = True,null = True)
    symbol = models.CharField(max_length = 10)
    transaction_amount=models.IntegerField()

    def __str__(self):
        return self.symbol



class TransactionSummary(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, null =True, blank = True)
    symbol = models.CharField(max_length = 10)
    symbol_total=models.IntegerField()
    absolute_symbol=models.IntegerField()

    def __str__(self):
        return self.symbol




    # def transactions_totals(request):
    #     t=Trasaction()
    #     transaction_numbers=t.objects.filter(symbol__isnull=True).aggregate(Sum('symbol'))
    #     print(transaction_numbers)

# def cart_item_pre_save_receiver(sender,instance,*args,**kwargs):
#     quantity=instance.quantity
#     if int(quantity)>=1:
#         price=instance.variation.get_price()
#         line_item_total=Decimal(quantity)*Decimal(price)
#         instance.line_item_total=line_item_total
#         #This will be our bottomline subtotal for CartItem
#
# pre_save.connect(cart_item_pre_save_receiver,sender = CartItem)
#
# def cart_item_post_save_receiver(sender,instance,*args,**kwargs):
#     instance.cart.update_subtotal()
#
# post_save.connect(cart_item_post_save_receiver,sender=CartItem)
