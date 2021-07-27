from django.db import models

from django.core.serializers.json import DjangoJSONEncoder


class Material(models.Model):

    name = models.CharField(max_length=250, blank=True)
    material_type = models.CharField(max_length=250, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
