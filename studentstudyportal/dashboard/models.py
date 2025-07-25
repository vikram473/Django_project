from gc import is_finalized
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Creating Notes database
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
# you want to show the title 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"
    
 # Creating Homework database 
class Homework(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    
    def __str__(self):
        return  self.title
     
# creating todo database
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

