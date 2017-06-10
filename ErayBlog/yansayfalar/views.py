from django.shortcuts import render
from .models import YanSayfalar

# Create your views here.
def home(request):
    yansayfalar = YanSayfalar.objects
    return render(request, 'yansayfalar/home.html', {'yansayfalar':yansayfalar})

def hakkinda(request):
    return render(request, 'yansayfalar/hakkinda.html',{})

def contact(request):
    return render (request, 'yansayfalar/contact.html')
