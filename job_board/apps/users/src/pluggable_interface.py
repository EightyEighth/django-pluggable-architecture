from .models import Recruiter
from chassis.apimanage import build_driver_api


class PluggableAPI:

    @staticmethod
    def get_recruiters():
        return Recruiter.objects.all().values()
