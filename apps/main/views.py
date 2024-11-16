from django.shortcuts import render
from .models import Personal, Home

# Create your views here.

def main(request):
    home = Home.objects.latest('id')
    main = Personal.objects.all()[:3]
    return render(request, 'index.html', locals())