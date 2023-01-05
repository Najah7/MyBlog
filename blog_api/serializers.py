from rest_framework import serializers


from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    """投稿記事用のシンプルなシリアライザ（ただのモデルの型に沿ったバリデーションのみ）"""

    # TODO:バリデーションの内容を考える。

    class Meta:
        model = BlogPost
        fields = '__all__'
