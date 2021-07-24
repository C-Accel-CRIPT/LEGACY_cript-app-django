from django.shortcuts import render

from api.models import Material


def index(request):
    """View function for home page of searh app"""

    material_list = [m for m in Material.objects.values()]
    context = {"matlist": material_list}

    return render(request, "index.html", context)
