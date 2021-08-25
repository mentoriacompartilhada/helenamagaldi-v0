from django.db import models


class Client(models.Model):
    name = models.CharField(max_length= 240)
    family_name = models.CharField(max_length= 300)
    age = models.IntegerField(max_length=3)
    nickname = models.CharField(max_length=10)
    password = models.CharField(max_length=7)


