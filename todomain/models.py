from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.TextField()
    is_delete = models.BooleanField(default=0)
    status = models.BooleanField(default=1)