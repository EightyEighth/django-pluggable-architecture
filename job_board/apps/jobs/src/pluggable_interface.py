from .models import Job


class PluggableAPI:

    @staticmethod
    def change_jobs_owner(old_recruiter_id, new_recruiter_id):
        Job.objects.filter(
            recruiter_id=old_recruiter_id
        ).update(recruiter_id=new_recruiter_id)
