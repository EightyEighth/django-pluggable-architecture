from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Candidate(models.Model):
    # relate with User model
    email = models.EmailField(unique=True, null=False)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_open_for_jobs = models.BooleanField(default=True)


class Recruiter(models.Model):
    # relate with User model
    email = models.EmailField(unique=True, null=False)
    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_open_for_hiring = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
