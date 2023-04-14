from django.db import models
from datetime import date
from tinymce import models as tinymce_models

# Create your models here.
class addPost(models.Model):
    slug = models.CharField(max_length=30, null=True)
    image = models.CharField(max_length=15, null=True)
    author = models.CharField(max_length=15, null=True)
    date = models.DateField(("Date"), default=date.today)
    title =models.CharField(max_length=50, null=True)
    shortContent = models.TextField(null=True)
    content = tinymce_models.HTMLField()
    
    def __str__(self):
	    return self.slug




