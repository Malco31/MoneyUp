from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Entry, Wages

from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ClockoutForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['user', 'hours', 'minutes', 'date']

class WageForm(ModelForm):
    class Meta:
        model = Wages
        fields = ['user', 'payrate']



        


