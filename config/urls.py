"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from app.views import frontpage, add_wage, signup, myaccount, signin, signout, edit_profile, clockout, admin_account, delete_entry, delete_user, view_user, clear_money, admin_delete_entry



urlpatterns = [
    path('', signin, name='login'),
    path('admin/', admin.site.urls),
    path('frontpage/', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signout/', signout, name='signout'),
    path('myaccount/', myaccount, name='myaccount'),
    path("myaccount/delete/<int:id>/", delete_entry, name ="delete"),
    
    
    path('admin_account/', admin_account, name='admin_account'),
    path('admin_account/delete/<username>/', delete_user, name='delete_user'),
    path('admin_account/clear/<username>/', clear_money, name='clear_money'),
    path('admin_account/view/<user>/', view_user, name='view_user'),
    
    path('wage/', add_wage, name='wage'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('clockout/', clockout, name='clockout'),
    
]
