from django.contrib import admin

# Register your models here.

from .models import Airplane, Airport, Passenger

admin.site.register(Airplane)
admin.site.register(Airport)
admin.site.register(Passenger)