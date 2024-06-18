from django.db import models
from catagories.models import Category
# Create your models here.
class task(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField(max_length=250)
    Task_Assign_Date = models.DateField()
    catagory= models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.taskTitle