from django.db import models

from exams.models import Assessment
from accounts.models import User

class Question(models.Model):

    question_number = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=200)
    description = models.TextField()
    score = models.PositiveIntegerField()
    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE)
    sample_input = models.TextField(null=True)
    sample_output = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        last_quest_objects = Question.objects.filter(assessment=self.assessment).last()

        if last_quest_objects:
            self.question_number = last_quest_objects.question_number +1

        else:
            self.question_number = 1

        return super().save(*args,**kwargs)