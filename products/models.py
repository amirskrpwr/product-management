from django.db import models

class Order(models.Model):
    date = models.DateField()
    customerName = models.CharField(max_length=120)

    def __str__(self):
        return ("{0:s}{1:s}".format(self.customerName,"'s order"))

class Product(models.Model):
    orders = models.ManyToManyField(Order)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)

    def __str__(self):
        return (self.title)



    
    