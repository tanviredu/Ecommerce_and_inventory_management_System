from django.db import models


class Device(models.Model):
    type_of_device = models.CharField(max_length=200, blank=False)
    price = models.PositiveIntegerField()
    status = models.CharField(max_length=200, default="SOLD")
    issue = models.CharField(max_length=200, default='No issue')

    def __str__(self):
        return 'TYPE : {}   PRICE : {}'.format(self.type_of_device, self.price)


class Laptop(Device):
    pass


class Desktop(Device):
    pass


class Mobile(Device):
    pass
