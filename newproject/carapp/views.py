from django.shortcuts import render
from .models import Car

# Create your views here.

def car_list(request):
    cars = Car.objects.all().order_by('year')
    return render(request, 'garage/car_list.html', {'cars': cars})

