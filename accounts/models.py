from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone = models.CharField(max_length=12,unique=True)

    ROLE_CHOICES = (
        ("student","student"),
        ("admin","admin")
    )

    role = models.CharField(max_length=100,choices=ROLE_CHOICES,default="student")



class StudentProfile(models.Model):

    skills = models.CharField(max_length=200,null=True)
    qualification = models.CharField(max_length=200,null=True)
    passoutyear = models.CharField(max_length=20,null=True)
    githuburl = models.URLField(null=True)
    linkedurl = models.URLField(null=True)
    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")    

from django.db.models.signals import post_save


def create_student_profile(sender,instance,created,*args,**kwargs):
    if created and instance.role == "student":
        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,sender=User)

# to send mail automatically when new user account is created

from django.core.mail import send_mail

def send_invitaion_mail(sender,instance,created,*args,**kwargs):
    if created and instance.role == "student":
        send_mail(
                    "Account creation Confirmation",
                    "You have successfully created account in codepilot",
                    "jainjohnson14@gmail.com",
                    ["greenrazor.gr@gmail.com"],
                )

post_save.connect(send_invitaion_mail,sender=User)