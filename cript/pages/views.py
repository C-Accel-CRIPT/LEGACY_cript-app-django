from django.shortcuts import render

from api.models import Material


def index(request):
    """View for the home page"""
    material_list = [m for m in Material.objects.values()]
    # change key names to look pretty on frontend
    material_list = [
        {k.title().replace("_", " "): v for k, v in m.items()}
        for m in material_list
    ]

    context = {"matlist": material_list}

    return render(request, "pages_index.html", context)


def about(request):
    """View for the about page"""
    return render(request, "pages_about.html", {})
