from django.contrib import admin

# Register your models here.
from .models import Facts , Service



admin.site.register(Facts)
admin.site.register(Service)