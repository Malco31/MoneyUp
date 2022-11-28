from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Entry

from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ClockoutForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['user', 'hours', 'minutes', 'date']


        






    # <!-- <div class="columns">
    #     <div class="column is-2">
    #         <div class="media mb-4">
    #             <div class="media-left">

    #             </div>

    #             <div class="media-content">
    #                 <p class="title is-3">{% firstof user.get_full_name user.username %}</p>
    #                 <p class="subtitle is-6">{{ user.email }}</p>
    #             </div>
    #         </div>

    #         <a href="#" class="button is-info">Edit profile</a>
    #         <a href="{% url 'logout' %}" class="button is-danger">Log out</a>
    #     </div>
    # </div> -->