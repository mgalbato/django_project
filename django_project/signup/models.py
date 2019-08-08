from django.db import models
from django.utils import timezone


class City(models.Model):
    population = models.IntegerField()
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)

    def __str__(self):
        return self.city + ", " + self.state

class Subscriber(models.Model):
    email = models.CharField(max_length=320)
    date_subscribed = models.DateTimeField(default=timezone.now)
    location = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
