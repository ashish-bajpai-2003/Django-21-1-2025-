from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request , 'home.html')

def about(request):
    return render(request , 'about.html')

def index(request):
    return render(request , 'index.html')
