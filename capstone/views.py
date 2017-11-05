from django.shortcuts import render

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
    return render(request,'portfolio.html')
