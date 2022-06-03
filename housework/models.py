from accounts.models import CustomUser
from django.db import models

class Purchases(models.Model):
    """買ったものモデル"""

    my_purchases = models.CharField(verbose_name='商品', max_length=10, blank=True, null=True)

    def __str__(self):
        return self.my_purchases


class Housework(models.Model):
    """家事モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    what_i_bought = models.ManyToManyField(Purchases, verbose_name='買った物')
    bought_items = models.BooleanField(verbose_name='買ったもの', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Housework'

    def __str__(self):
        return self.title