from django.contrib.auth.models import User
from django.db import models
from datetime import date
# from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


# class IntegerRangeField(models.IntegerField):
#     def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
#         self.min_value, self.max_value = min_value, max_value
#         models.IntegerField.__init__(self, verbose_name, name, **kwargs)
#     def formfield(self, **kwargs):
#         defaults = {'min_value': self.min_value, 'max_value':self.max_value}
#         defaults.update(kwargs)
#         return super(IntegerRangeField, self).formfield(**defaults)


hour_choices=[
    (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), 
    (10,10), (11,11), (12,12),
]

minute_choices=[
    (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), 
    (10,10), (11,11), (12,12),
]


        
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hours=models.IntegerField(default=0, choices=hour_choices)
    
    minutes=models.IntegerField(default=0, choices=minute_choices)
    date=models.CharField(max_length=10)

class Wages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payrate = models.DecimalField(decimal_places=2, max_digits=4)
    

    