from .models import Company


class PluggableAPI:

    @staticmethod
    def get_recruiters(company_id):
        return Company.objects.filter(
            id=company_id
        ).last().recruiter_set.values_list('id', flat=True)

    @staticmethod
    def get_companies():
        return Company.objects.all().values('id', 'name')
