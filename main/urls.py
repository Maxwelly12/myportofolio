from django.urls import path

from main.views import (
    show_main, 
    show_experience, 
    show_education,
    show_projects, 
    get_projects_json, 
    delete_project,
    create_project,
    create_testimony,
    show_testimony,
    delete_testimony,
    get_testimonys_json,
    register, 
    login_user,
    logout_user, 
    toggle_star,
    toggle_star_testimony,
    show_univcourses,
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
    path("testimony/add/", create_testimony, name="create_testimony"),
    path("testimony/", show_testimony, name="show_testimony"),
    path("testimony/<uuid:testimony_id>/delete/", delete_testimony, name="delete_testimony"),    
    path('api/testimony/', get_testimonys_json, name='get_testimonys_json'),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path(
    "projects/<uuid:project_id>/star/",
    toggle_star,
    name="toggle_star",
), 
    path(
        "testimony/<uuid:testimony_id>/star/",
        toggle_star_testimony,
        name="toggle_star_testimony",
    ),
    path("univcourse/", show_univcourses, name="show_univcourse"),
]