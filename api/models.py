from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(unique=True,blank=False,null=False)
    def __str__(self):
        return self.name

class Task(models.Model):
    description  = models.TextField(unique=True,blank=False,null=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
