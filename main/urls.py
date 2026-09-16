from django.urls import path

from main.views import (
    show_main, 
    show_experience, 
    show_education,
    show_projects, 
    get_projects_json, 
    delete_project,
    create_project
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"), 
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
]