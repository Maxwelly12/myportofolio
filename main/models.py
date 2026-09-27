from django.db import models

# Create your models here.
import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model):
    EDUCATION_CHOICES = [
        ('middle', 'Middle School'),
        ('high_school', 'High School'),
        ('bachelor', 'Bachelor'),
    ]   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution_name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EDUCATION_CHOICES, default='bachelor')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(default=timezone.now)    
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.institution_name

    @property
    def is_ongoing(self):
        return self.ended_at is None

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )

    def __str__(self):
        return self.title

class Testimony(models.Model) :
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    description = models.TextField()
    message_date = models.DateTimeField(default=timezone.now)    

    def __str__(self) :
        return self.name

class Univcourses(models.Model) :
    UCOURSES_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'), 
        ('4', '4'), 
        ('5', '5'),
        ('6', '6'), 
        ('7', '7'), 
        ('8', '8'), 
        ('choice', 'CHOICE'), 
    ]

    UCOURSES_CATEGORY = [
        ('datascience', 'DataScience'),
        ('cybersecurity', 'CyberSecurity'),
        ('business', 'Business'),
        ('moral', 'Moral'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 255)
    semester = models.CharField(max_length=10, choices=UCOURSES_CHOICES, default='1')
    category = models.CharField(max_length=255, choices=UCOURSES_CATEGORY, default='business')
    ended_at = models.DateTimeField(blank=True, null=True)

    @property
    def isfinished(self) :
        return self.ended_at  is None
