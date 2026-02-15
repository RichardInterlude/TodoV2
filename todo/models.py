from django.db import models
from django.contrib.auth.models import User



TASK_STATUS = (('pending','Pending'),('in progress','In Progress'),('completed','Completed'))

PRIORITY_LEVELS = (('low','Low'),('medium','Medium'),('urgent','Urgent'))


    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank= True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.title

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, choices = TASK_STATUS, default='pending')
    priority = models.CharField(max_length=255, choices=PRIORITY_LEVELS, default ='medium',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank= True)
    due_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title