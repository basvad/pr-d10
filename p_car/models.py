from django.db import models

#модель автомобиля
class Car(models.Model):
    MECHANIC, AUTO, ROBOT = range(3)
    KPP_CHOICES = [
        [MECHANIC, "механика"],
        [AUTO, "автомат"],
        [ROBOT, "робот"],
    ]
    #производитель (BMW, Audi, Tesla и т.д.) (CharField)
    manufacturer = models.CharField(max_length=255)
    #модель авто (S, TT, X6 и т.д.) (CharField)
    model = models.CharField(max_length=255)
    #год выпуска (IntegerField)
    year = models.IntegerField()
    #коробка передач (SmallIntegerField with choices "механика", "автомат", "робот")
    kpp = models.SmallIntegerField(choices=KPP_CHOICES)
    #цвет
    color = models.CharField(max_length=255)