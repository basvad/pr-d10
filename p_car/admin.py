from django.contrib import admin
from p_car.models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display=('manufacturer','model','year','kpp','color')