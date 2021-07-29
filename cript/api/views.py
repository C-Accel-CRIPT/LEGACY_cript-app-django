from django.shortcuts import render

from rest_framework import viewsets, generics

from .serializers import MaterialSerializer
from .models import Material


def index(request):
    """View for the API index.html homepage"""
    return render(request, "api_index.html", {})


def about(request):
    """View for the API index.html homepage"""
    return render(request, "api_about.html", {})


class MaterialList(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
