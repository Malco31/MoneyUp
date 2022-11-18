from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Userprofile(models.Model):
    user = models.ForeignKey(User, related_name="userprofile", on_delete=models.CASCADE)

    def registered_time(self):
        return 0


        
class Entry(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    minutes=models.IntegerField(default=0)
    is_tracked=models.BooleanField(default=False)
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField()

    