from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Education, Project
from main.forms import ProjectForm

# Create your views here.

def show_main(request):
    context = {
        "name": "Maxwelly F.H. Simatupang",
        "npm": "2506584294",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "A Computer Science Student who embarks on technology ,especialy with "
            "big data and data science, and business ,especialy with digital marketing "
            "and public relations. Have experience with some potition in public relations "
            "and digital marketing that give me a knowledge in communication and analitical "
            "thinking. Now, greatly to study more on data science or digital marketer "
            "through out organization or boot camp."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Maxwelly F.H. Simatupang",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request) :
    context = {
        "name": "Maxwelly F.H. Simatupang",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Burhan",   
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Maxwelly F.H.  Simatupang",
        "project_list": Project.objects.all(),
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")