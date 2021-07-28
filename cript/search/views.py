from django.shortcuts import render

from api.models import Material


def index(request):
    """View function for home page of search app"""
    material_list = [m for m in Material.objects.values()]
    # change key names to look pretty on frontend
    material_list = [
        {k.title().replace("_", " "): v for k, v in m.items()}
        for m in material_list
    ]
    context = {"matlist": material_list}
    return render(request, "index.html", context)


def about(request):
    """view function for search - about page"""
    return render(request, "about.html", {})
