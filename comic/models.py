from django.db import models


class Comic(models.Model):
    name = models.CharField(max_length=100)
    numberOfPages = models.IntegerField()
    creationDate = models.DateField()


# Create your models here.
