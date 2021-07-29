from django.urls import include, path

# from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r"materials", views.MaterialViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", views.index, name="api_index"),
    path("about/", views.about, name="api_about"),
    path("materials/", views.MaterialList.as_view()),
    path("materials/<int:pk>/", views.MaterialDetail.as_view()),
    # path("keywords/", views.KeywordList.as_view()),
    # path("keywords/<int:pk>/", views.KeywordDetail.as_view()),
]
