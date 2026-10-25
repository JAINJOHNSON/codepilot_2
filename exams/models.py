from django.db import models

from accounts.models import User

from datetime import datetime,time,timedelta

class Assessment(models.Model):

    title = models.CharField(max_length=200)

    batch = models.CharField(max_length=200)

    LANGUAGE_CHOICES = (
        ("python","python"),
        ("react","react"),
        ("html","html"),
        ("css","css"),
        ("javascript","javascript")
    )

    language = models.CharField(max_length=200,choices=LANGUAGE_CHOICES)

    exam_date = models.DateField(null=False)

    start_time = models.TimeField(null=False)

    duration = models.PositiveIntegerField(null=False)

    end_time = models.TimeField(null=True)

    STATUS_CHOICES = (
        ("pending","pending"),
        ("ongoing","ongoing"),
        ("completed","completed"),
        ("submitted","submitted")
    )

    status = models.CharField(max_length=200,choices=STATUS_CHOICES,default="pending")

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):

        end_datetime = datetime.combine(self.exam_date,self.start_time)+timedelta(hours=self.duration)

        self.end_time = end_datetime.time()

        return super().save(*args,**kwargs)