from django.db import models
from django.utils import timezone
# Create your models here.
class Car(models.Model):
    Fuel_Type = [
        ('', 'Select Fuel Type'),
        ('gas', 'Gas'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('lp_gas', 'LP Gas'),
    ]
    Roof_type = [
        ("", "Select Roof Type"),
        ('convertible', 'Convertible'),
        ('hardtop', 'Hardtop'),
        ('sunroof', 'Sunroof'),
    ]

    vin = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    door_count = models.SmallIntegerField()
    roof_type = models.CharField(max_length=50, choices=Roof_type, default='')
    year = models.SmallIntegerField()
    fuel_type = models.CharField(max_length=50, choices=Fuel_Type, default='')
    post_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.color} {self.make} {self.model}"