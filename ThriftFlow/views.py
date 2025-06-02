from django.shortcuts import render

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def investments(request):
    return render(request, 'base/investments.html')

def profits(request):
    return render(request, 'base/profits.html')

def savings(request):
    return render(request, 'base/savings.html')

def blog(request):
    return render(request, 'base/blog.html')

def daylo(request):
    return render(request, 'base/daylo.html')


# Create your views here.
