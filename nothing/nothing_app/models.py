from django.db import models


class Dog(models.Model):
    name = models.Charfield(max_length = 255)
    Dog = models.BooleanField(True)
    Born = models.DateTimeField(auto_now_add = True)

    def name(self):
        return self.name

class Person(models.Model):
    Application = models.TextField()
    age = models.IntegerField(default = 14)
    adult = models.BooleanField(default = True)

    def Adult_Or_Not(self):
        return self.adult

class Plane(models.Model):
    name = models.Charfield(max_length = 255)
    Description = models.TextField()
    Safe = models.BooleanField(default = True)

    def get_safety(self):
        return self.Safe
# Create your models here.
