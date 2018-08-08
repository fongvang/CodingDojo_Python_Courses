from __future__ import unicode_literals
from django.db import models

class courseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be at least 5 characters"
        if len(postData['description']) < 15:
            errors["description"] = "Blog description should be at least 15 characters"
        return errors

# Create your models here.
class courses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

#   added messages
    objects = courseManager()