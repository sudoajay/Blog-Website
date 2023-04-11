from django.db import models
from datetime import date

# Create your models here.
class addPost(models.Model):
    slug = models.CharField(max_length=30, null=True)
    image = models.CharField(max_length=15, null=True)
    author = models.CharField(max_length=15, null=True)
    date = models.DateField(("Date"), default=date.today)
    title =models.CharField(max_length=30, null=True)
    shortContent = models.TextField(null=True)
    content = models.TextField(null=True)
    def __str__(self):
	    return self.slug


