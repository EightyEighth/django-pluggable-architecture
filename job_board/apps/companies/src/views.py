from django.shortcuts import render, redirect
from .models import Company


def list_of_companies(request):

    return render(
        request,
        'companies.html',
        context={'companies': Company.objects.all()}
    )


def add_company(request):
    if request.method == 'POST':
        Company.objects.create(
            name=request.POST.get('name'),
            about=request.POST.get('about'),
            employee_count=request.POST.get('employee_count')
        )
    return redirect('companies')


def delete_company(request, company_id):
    company = Company.objects.get(id=company_id)
    company.delete()
    return redirect('companies')
