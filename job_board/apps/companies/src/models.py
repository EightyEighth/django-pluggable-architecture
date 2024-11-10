from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    class Domain(models.TextChoices):
        GAMBLING = "gambling", _("Gambling")
        GAMEDEV = "gamedev", _("Gamedev")
        FINTECH = "fintech", _("Fintech")
        OUTSOURCE = "outsource", _("Outsource")
        ECOMMERCE = "ecommerce", _("Ecommerce")

    name = models.CharField(max_length=255)
    about = models.TextField()
    domain = models.CharField(max_length=30, choices=Domain)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    location = models.CharField(max_length=255)
    website = models.URLField()
    employee_count = models.PositiveIntegerField()
    is_verified = models.BooleanField(default=False)
    is_hiring = models.BooleanField(default=False)
    has_internship = models.BooleanField(default=False)

