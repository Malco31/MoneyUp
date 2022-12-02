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
    (10,10), (11,11), (12,12), (13,13), (14,14), (15,15), (16,16),
    (17,17), (18,18), (19,19), (20,20), (21,21), (22,22), (23,23),
    (24,24), (25,25), (26,26), (27,27), (28,28), (29,29), (30,30),
    (31,31), (32,32), (33,33), (34,34), (35,35), (36,36), (37,37),
    (38,38), (39,39), (40,40), (41,41), (42,42), (43,43), (44,44),
    (45,45), (46,46), (47,47), (48,48), (49,49), (50,50), (51,51),
    (52,52), (53,53), (54,54), (55,55), (56,56), (57,57), (58,58),
    (59,59),
]


        
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hours=models.IntegerField(default=0, choices=hour_choices)
    
    minutes=models.IntegerField(default=0, choices=minute_choices)
    date=models.CharField(max_length=10)

class Wages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payrate = models.DecimalField(decimal_places=2, max_digits=4)
    

    