from django.contrib.gis.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Request(models.Model):

    #details of person requesting
    requestor=models.CharField(max_length=100)
    location = models.PointField(srid=4326,geography=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    #requirement details
    requirement = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    priority = models.IntegerField(default=0);
    created = models.DateTimeField(auto_now_add=True)

    #whether address/current location is shared or not
    addressAllowed = models.BooleanField()

    def __str__(self):
        return self.requestor+str(self.created);
