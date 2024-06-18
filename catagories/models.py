from django.db import models
from task.models import task

# Create your models here.
class Category(models.Model):
    Category_Name = models.CharField(max_length=100)
    catagory = models.ManyToManyField(task)
    
    def __str__(self):
        return self.Category_Name