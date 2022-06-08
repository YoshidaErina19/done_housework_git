from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

# Create your models here.

class Grocery(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    checkbox_1 = models.CharField(max_length=10, default='unchecked')
    checkbox_2 = models.CharField(max_length=10, default='unchecked')
    checkbox_3 = models.CharField(max_length=10, default='unchecked')
    checkbox_created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    checkbox_updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Grocery'

    def __str__(self):
        return self.checkbox_created_at
