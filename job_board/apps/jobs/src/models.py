from django.db import models


class Job(models.Model):
    position = models.CharField(max_length=255)
    description = models.TextField()
    recruiter = models.ForeignKey("users.Recruiter", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_remote = models.BooleanField(default=False)
    location = models.CharField(max_length=255)
    salary_from = models.DecimalField(max_digits=10, decimal_places=2)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    published_at = models.DateTimeField()
