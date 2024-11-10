from django.shortcuts import render, redirect
from chassis.apimanage import build_driver_api
from .models import Recruiter


def list_users(request):
    users = Recruiter.objects.all()
    company_api = build_driver_api('companies.api', 'api')

    companies_list = company_api.get_companies()

    return render(
        request,
        'users.html',
        context={'users': users, 'companies': companies_list}
    )


def add_user(request):
    if request.method == 'POST':
        Recruiter.objects.create(
            email=request.POST.get('email'),
            company_id=request.POST.get('company')
        )
    return redirect('users')


def delete_user(request, user_id):
    user = Recruiter.objects.get(id=user_id)
    user.delete()
    return redirect('users')


def change_company(request, user_id):
    recruiter_id = user_id
    new_company_id = request.POST.get('company')
    new_jobs_owner_id = request.POST.get('new_jobs_owner')

    job_api = build_driver_api('jobs.api', 'api')
    company_api = build_driver_api('companies.api', 'api')

    old_jobs_owner = Recruiter.objects.filter(id=recruiter_id).last()
    new_jobs_owner = None

    if new_jobs_owner_id:
        new_jobs_owner = Recruiter.objects.filter(id=new_jobs_owner_id).last()

    if not new_jobs_owner:
        company_recruiter_ids = company_api.get_recruiters(
            old_jobs_owner.company_id)

        if company_recruiter_ids:
            new_jobs_owner = Recruiter.objects.filter(
                id__in=company_recruiter_ids).exclude(
                id=recruiter_id).last()

    job_api.change_jobs_owner(
        old_recruiter_id=recruiter_id,
        new_recruiter_id=new_jobs_owner.id if new_jobs_owner else None
    )

    old_jobs_owner.company_id = new_company_id
    old_jobs_owner.save()

    return redirect('users')
