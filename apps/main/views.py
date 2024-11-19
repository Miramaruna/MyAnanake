from django.shortcuts import render
from .models import Personal, Home
from .serializers import HomeSerilizer, PersonalSerilizer
from rest_framework.generics import (ListAPIView, CreateAPIView, 
                                     UpdateAPIView, DestroyAPIView, RetrieveAPIView,
                                     ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.pagination import PageNumberPagination

# Create your views here.

def main(request):
    home = Home.objects.latest('id')
    main = Personal.objects.all()[:3]
    return render(request, 'index.html', locals())

class Pagination(PageNumberPagination):
    max_page_size = 10
    page_size = 3

class HomeListAPI(ListAPIView):   
    queryset = Home.objects.all()
    serializer_class = HomeSerilizer

class PersonalListAPI(ListAPIView):   
    queryset = Personal.objects.all()
    serializer_class = PersonalSerilizer

class PersonalCreateAPI(CreateAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerilizer

class PersonalRetrieveAPI(RetrieveAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerilizer

class PersonalUpdateAPI(UpdateAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerilizer

class PersonalDestroyAPI(DestroyAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerilizer

class PersonalListCreateAPI(ListCreateAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerilizer

class PersonalMultiAPI(RetrieveUpdateDestroyAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerilizer