from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Patients(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)


    patient_name=models.CharField(max_length=100)
    patient_age=models.IntegerField()
    choice=[
        ('M','Male'),
        ('F','Femle'),
        ('O','Other')
    ]
    gender=models.CharField(max_length=1,choices=choice)
    content=models.CharField(max_length=11)
    address=models.TextField()
    time=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.patient_name
            



