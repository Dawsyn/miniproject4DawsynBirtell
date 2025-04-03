from django.db import models
from django.contrib import admin
#from .models import Contest
# Create your models here.


class ContestForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=1)
    contest = models.ForeignKey('Contest', on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")

    contest = models.ForeignKey('Contest', on_delete=models.CASCADE)  
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
class Contest(models.Model):
    contest_name = models.CharField(max_length=200)
    contest_description = models.TextField()
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.contest_description