from django.shortcuts import render

from rest_framework import viewsets

from .serializers import MaterialSerializer
from .models import Material


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all().order_by("name")
    serializer_class = MaterialSerializer
