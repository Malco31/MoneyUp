from django.contrib import admin

# Register your models here.

from .models import Entry, Wages

admin.site.register(Entry)

admin.site.register(Wages)