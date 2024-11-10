"""
URL configuration for job_board project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.companies.src import views as companies_views
from apps.users.src import views as users_views
from apps.jobs.src import views as jobs_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", companies_views.list_of_companies, name="companies"),
    path("companies/add/", companies_views.add_company, name="add_company"),
    path("companies/delete/<int:company_id>/", companies_views.delete_company, name="delete_company"),
    path("users/", users_views.list_users, name="users"),
    path("users/add/", users_views.add_user, name="add_user"),
    path("users/delete/<int:user_id>/", users_views.delete_user, name="delete_user"),
    path("users/change_company/<int:user_id>/", users_views.change_company, name="change_company"),
    path("jobs/", jobs_views.list_jobs, name="jobs"),
    path("jobs/add/", jobs_views.add_job, name="add_job"),
    path("jobs/delete/<int:job_id>/", jobs_views.delete_job, name="delete_job"),
]
