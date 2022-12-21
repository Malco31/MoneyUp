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
from app import views
from app.views import * 



urlpatterns = [
    path('', views.signin, name='login'),
    path('frontpage/', views.frontpage, name='frontpage'),
    path('signout/', views.signout, name='signout'),
    
    # User Views
    path('myaccount/', views.myaccount, name='myaccount'),
    path("myaccount/delete/<int:id>/", views.delete_entry, name ="delete"),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('clockout/', views.clockout, name='clockout'),

    # Admin Views
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('admin_account/', views.admin_account, name='admin_account'),
    path('admin_account/delete/<username>/', views.delete_user, name='delete_user'),
    path('admin_account/clear/<username>/', views.clear_money, name='clear_money'),
    path('admin_account/view/<user>/', views.view_user, name='view_user'),
    path('wage/', views.add_wage, name='wage'),
    
    
    
]
