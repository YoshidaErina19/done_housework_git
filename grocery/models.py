from django.db import models

# Create your models here.

class CheckBox(models.Model):
    checkbox_1 = models.CharField(max_length=10, default='unchecked')
    checkbox_2 = models.CharField(max_length=10, default='unchecked')
    checkbox_3 = models.CharField(max_length=10, default='unchecked')