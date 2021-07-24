from django.db import models


class Material(models.Model):

    name = models.CharField(max_length=200)
    material_type = models.CharField(max_length=200)
    notes = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
