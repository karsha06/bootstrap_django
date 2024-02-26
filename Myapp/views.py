from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def blog (request):
    return render(request, 'blog-single.html')

def icons(request):
    return render(request, '404.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

