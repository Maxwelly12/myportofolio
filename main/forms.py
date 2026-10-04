from django.forms import ModelForm, TextInput, Textarea, URLInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()
    
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

    def clean_name(self):
        name = strip_tags(self.cleaned_data["name"]).strip()
        if not name:
            raise ValidationError("Name cannot consist only of HTML tags.")
        return name

    def clean_relationship(self):
        relationship = strip_tags(self.cleaned_data["relationship"]).strip()
        if not relationship:
            raise ValidationError("Relationship cannot consist only of HTML tags.")
        return relationship

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"]).strip()
        if not description:
            raise ValidationError("Testimony cannot consist only of HTML tags.")
        return description
        
