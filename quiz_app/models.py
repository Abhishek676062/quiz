from django.db import models

class Quiz(models.Model):
    question = models.TextField()
    options = models.JSONField()
    right_answer = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, default='inactive')

    class Meta:
        app_label = 'quiz_app'

    def __str__(self):
        return self.question
