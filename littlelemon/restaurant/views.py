from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from .models import Booking, Menu
from .serializer import MenuSerializer, BookingSerializer


def say_hello(request):
    return HttpResponse("Hello world")

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'pk'

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

