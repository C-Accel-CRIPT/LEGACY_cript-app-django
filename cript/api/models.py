from django.db import models


class Keyword(models.Model):
    choices = (
        ("amorphous", "amorphous"),
        ("thermoset", "thermoset"),
        ("elastomer", "elastomer"),
    )
    name = models.CharField(max_length=250, choices=choices, unique=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    """
    The material class.

    When searching through materials, use
    Material.objects.filter(name__text_search='styrene')

    """

    name = models.CharField(max_length=250, blank=True)
    material_type = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    keywords = models.CharField(max_length=2000, blank=True)

    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
