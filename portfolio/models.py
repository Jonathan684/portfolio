from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/image")
    url = URLField(blank=True)

# Models for report

class Report(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to="portfolio/image")
    description = CharField(max_length=250)
    report = CharField(max_length=50,blank=True)