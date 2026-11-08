from django.urls import path

from main import api_views

app_name = "api"

urlpatterns = [
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
    path("projects/<uuid:project_id>/star/", api_views.project_star, name="project-star"),
    path("testimony/", api_views.testimony_list, name="testimony-list"),
    path("testimony/<uuid:testimony_id>/", api_views.testimony_detail, name="testimony-detail"),
    path("testimony/<uuid:testimony_id>/star/", api_views.testimony_star, name="testimony-star"),
]