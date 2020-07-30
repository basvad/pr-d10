from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from p_car.models import Car
from django.db.models import Q
from django.views.generic import TemplateView



def index(request):
    template = loader.get_template('index.html')
    params = request.GET
    #query с пустым Q-объектом
    query = Q()
    for key, value in params.items():
            if value and key in vars(Car):
                query &= Q(**{key: value})
    cars_data = {"cars": Car.objects.filter(query)}
    
    return HttpResponse(template.render(cars_data))

