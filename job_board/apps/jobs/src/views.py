from django.shortcuts import render, redirect
from django.utils import timezone
from chassis.apimanage import build_driver_api
from .models import Job


def list_jobs(request):
    jobs = Job.objects.all()
    user_api = build_driver_api('users.api', 'api')
    recruiters_list = user_api.get_recruiters()

    return render(
        request,
        'jobs.html',
        context={'jobs': jobs, 'recruiters': recruiters_list}
    )


def add_job(request):
    if request.method == 'POST':
        Job.objects.create(
            position=request.POST.get('position'),
            description=request.POST.get('description', ""),
            recruiter_id=request.POST.get('recruiter'),
            salary_from=request.POST.get('salary_from'),
            salary_to=request.POST.get('salary_to'),
            published_at=timezone.now()
        )
    return redirect('jobs')


def delete_job(request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()
    return redirect('jobs')
