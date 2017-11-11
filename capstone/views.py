from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from transaction.models import Transaction, TransactionSummary
from django.contrib.auth.models import User
from django.db.models import Sum

from django.http import JsonResponse
from instruments.models import Instrument


def home(request):
    return render(request,'home.html')

def aboutUS(request):
    return render(request,'aboutUS.html')

def ContactUS(request):
    return render(request,'ContactUS.html')

def Register(request):
    return render(request,'Register.html')

def specs(request):
    return render(request,'specs.html')

def portfolio(request):
    trans = TransactionSummary.objects.filter(user=request.user.id)
    context = {'object':trans}
    return render(request,'portfolio.html',context)

def transaction(request):
    trans = Transaction.objects.filter(user=request.user.id)
    context = {'object':trans}
    return render(request,'transactions.html',context)

def funds(request):
    return render(request,'funds.html')



@csrf_exempt
def purchase_made(request):
    """Purchase made accepts a POST request from our Trade Futures Contract
    Our if statment verifies that a POST request comes in and that the user is
    Authenticated. We then get each portion of the get request, storing them into
    variables. Lastly, we create an instance of the Transaction class and using the
    request object, we get our user, and add the seperate portions of the POST
    request into the database"""

    # multiplier = Instrument.objects.values_list('multiplier')[11][0]
    # print(multiplier)
    if request.method == 'POST' and request.user.is_authenticated():
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        symbol = request.POST.get('symbol')
        multiplier = request.POST.get('multiplier')
        if (int(quantity)!=0):
            t = Transaction()
            t.user = request.user
            t.symbol = symbol
            t.quantity = int(quantity)
            t.price = float(price)
            z=Instrument()
            z.multiplier = int(multiplier)
            t.transaction_amount= z.multiplier*t.quantity*t.price
            t.save()
            # transaction_list = Transaction.objects.values('symbol').annotate(total=Sum('transaction_amount'))
            transaction_list = Transaction.objects.filter(user=request.user.id).values('symbol').annotate(total=Sum('transaction_amount'))
            TransactionSummary.objects.filter(user=request.user.id).delete()
            for item in range(len(transaction_list)):
                y=TransactionSummary()
                y.user=request.user
                y.symbol=transaction_list[item]['symbol']
                y.symbol_total=transaction_list[item]['total']
                y.absolute_symbol=abs(y.symbol_total)
                y.save()
            print(transaction_list)
            # print(type(transaction_list))
            # print(transaction_list[0]['symbol'])
            return JsonResponse({'success':'true'})
        return
