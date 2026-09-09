from django.shortcuts import render

from main.models import Experience
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