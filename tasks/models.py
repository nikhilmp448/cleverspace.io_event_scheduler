from django.db import models
from users.models import Account


class Task(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start = models.DateField(null=True,blank=True)
    end = models.DateField(null=True,blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class IndividualTask(models.Model):
    task = models.ForeignKey(Task, related_name='individual_tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null = True,blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title






