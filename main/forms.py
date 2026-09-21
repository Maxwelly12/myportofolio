from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Project, Testimony

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class TestimonyForm(ModelForm) :
    class Meta:
        model = Testimony
        fields = [
            "name", 
            "relationship",
            "description",
        ]

        labels = {
            "name" :  "Name",
            "relationship" : "What is your relationship to Maxwelly  F.h. Simatupang",
            "description" : "Testimony", 
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "What is your name",
                    "maxlength": 255,
                }
            ),
            "relationship": TextInput(
                attrs={
                    "placeholder": "What is your relationship to Maxwelly  F.h. Simatupang",
                    "maxlength": 255,
                }   
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Give your testimony to Maxwelly F.H. Simatupang",
                    "rows": 3,
                }
            ),
        }
