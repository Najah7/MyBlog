from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        db_table = 'custom_user'

    gender = models.BooleanField(verbose_name='性別', null=True)
    age = models.IntegerField(verbose_name='年齢', null=True)
    profile_image = models.ImageField(verbose_name='プロフィール画像', null=True)
    favorite_programming_lang = models.CharField(verbose_name='好きなプログラミング言語', max_length=50)
    login_count = models.IntegerField(verbose_name='ログイン回数', default=0)



