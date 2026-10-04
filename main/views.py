import datetime

from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied       
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from main.models import Experience, Education, Project, Testimony, Univcourses
from main.forms import ProjectForm
from main.forms import ProjectForm, TestimonyForm


# Create your views here.

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
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
        "last_login" : last_login, 
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

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project has been added!")
        return redirect("main:show_projects")

    context = {
        "name": "Maxwelly F.H. Simatupang",   
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Maxwelly F.H. Simatupang",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project has been deleted!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def create_testimony(request):
    if not request.user.is_superuser :
        raise PermissionDenied
    
    form = TestimonyForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New testimony has been added!")
        return redirect("main:show_testimony")

    context = {
        "name": "Maxwelly F.H. Simatupang",   
        "form": form,
    }
    return render(request, "testimony_form.html", context)

def show_testimony(request):
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Maxwelly F.H.  Simatupang",
        "title_query": title_query,
        "form" : TestimonyForm(),
    }
    return render(request, "testimony.html", context)

def get_testimonys_json(request):
    title_query = request.GET.get("title", "").strip()
    testimonys = Testimony.objects.all()

    if title_query:
        testimonys = testimonys.filter(name__icontains=title_query)

    data = []
    for test in testimonys :
        starred_user = test.starred_by.all();
        is_starred = request.user in starred_user if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_user])

        data.append({
            "pk": str(test.id),
            "fields": {
                "name": test.name,
                "relationship": test.relationship,
                "description": test.description,
                "message_date": test.message_date,
                "star_count": starred_user.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_testimony(request, testimony_id):
    testimony = get_object_or_404(Testimony, pk=testimony_id)

    if request.method == "POST":
        testimony.delete()
        messages.success(request, "Testimony has been erased!")
        return redirect("main:show_testimony")

    return redirect("main:show_testimony")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":

        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

def show_univcourses(request):
    context = {
        "name": "Maxwelly F.H. Simatupang",
        "experience_list": Univcourses.objects.all(),
    }
    return render(request, "univcourse.html", context)

@login_required(login_url="/login/")
def toggle_star_testimony(request, testimony_id):
    testimony = get_object_or_404(Testimony, pk=testimony_id)

    if request.method == "POST":
        if request.user in testimony.starred_by.all():
            testimony.starred_by.remove(request.user)
        else:
            testimony.starred_by.add(request.user)

    return redirect("main:show_testimony")

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def create_testimony_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan testimony."},
            status=403,
        )

    form = TestimonyForm(request.POST)
    if form.is_valid():
        testimony = form.save()
        return JsonResponse(
            {"message": "Testimony berhasil ditambahkan.", "pk": str(testimony.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)