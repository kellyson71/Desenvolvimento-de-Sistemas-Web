from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def portfolio(request):
    return render(request, 'core/portfolio.html')
