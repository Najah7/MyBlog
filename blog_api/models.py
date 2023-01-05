import uuid

from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """
    投稿されたブログ記事のモデル

    NOTE:とりあえず必要なカラムを書いたので、まだ正規化などはしてない。
    """

    class Meta:
        db_table = 'book'
        ordering = []
        verbose_name = verbose_name_plural = '投稿記事'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=30, unique=True, null=False)
    # articleはファイルした方がいいかも
    article = models.TextField(verbose_name='記事')
    # TODO:django-imagekitに変更。
    # imageフィールドがapiでjsonで返せないのでそこの所をいい感じにする必要あり。（多分、画像のurlを送って、frontからgetしてもらう感じかな？）
    # thumbnail = models.ImageField(verbose_name='サムネ用の写真', null=True, upload_to='image/')
    short_description = models.CharField(verbose_name='軽い説明のテキスト', max_length=100, null=True)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日')
    n_goods = models.IntegerField(verbose_name='いいね', default=0)
