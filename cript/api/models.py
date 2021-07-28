from django.db import models

# from djongo.models.indexes import TextIndex

from django.core.serializers.json import DjangoJSONEncoder


class Material(models.Model):
    """The material class"""

    name = models.CharField(max_length=250, blank=True)
    material_type = models.CharField(max_length=250, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

    # class Meta:
    #    """Use this to set which fields to index for searches"""
    #
    #    indexes = [TextIndex(fields=["name", "material_type", "notes"])]


# when searching through materials, use
# Material.objects.filter(name__text_search='styrene')
