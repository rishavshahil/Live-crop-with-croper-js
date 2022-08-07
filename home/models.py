from django.db import models

# Create your models here.
class DemoUpload(models.Model):
    image = models.ImageField(upload_to = 'rishav/')