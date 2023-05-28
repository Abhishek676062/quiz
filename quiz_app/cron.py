from django_cron import CronJobBase, Schedule
from django.utils import timezone

from .models import Quiz

class UpdateQuizStatusCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'quiz_app.update_quiz_status_cron_job'

    def do(self):
        now = timezone.now()
        active_quizzes = Quiz.objects.filter(start_date__lte=now, end_date__gte=now, status='inactive')
        active_quizzes.update(status='active')

        finished_quizzes = Quiz.objects.filter(end_date__lt=now, status='active')
        finished_quizzes.update(status='finished')
