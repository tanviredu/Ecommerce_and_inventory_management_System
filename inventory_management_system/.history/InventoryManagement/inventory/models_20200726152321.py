from django.db import models


# this device class will be an abstract class
# we dont need to be present
##
class Device(models.Model):
    type_of_device = models.CharField(max_length=200, blank=False)
    price          = models.PositiveIntegerField()
    status         = models.CharField(max_length=200, default="SOLD")
    issue          = models.CharField(max_length=200, default='No issue')
    choices        = (
        ('AVAILABLE','Ready to Purchage'),
        ('SOLD','Item Sold'),
        ('Restocking','item restocking in few days')
    )

    def __str__(self):
        return 'TYPE : {}   PRICE : {}'.format(self.type_of_device, self.price)

    class Meta:
        abstract = True


class Laptop(Device):
    pass


class Desktop(Device):
    pass


class Mobile(Device):
    pass
