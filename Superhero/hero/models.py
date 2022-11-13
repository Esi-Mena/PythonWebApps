from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    description = models.TextField(default="None")
    image = models.CharField(max_length=200, default="None")
    strengths = models.CharField(max_length=200, default="None")
    weaknesses = models.CharField(max_length=200, default="None")

    def _str_(self):
        return self.identity

    def get_absolute_url(self):
            return reverse_lazy('hero_list')

