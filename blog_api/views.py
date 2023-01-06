from rest_framework import generics
from django_filters import rest_framework as filters

from .serializers import BlogPostSerializer
from .models import BlogPost


# Create your views here.


class BlogPostCreateAPIView(generics.CreateAPIView):
    """記事作成用のAPIクラス"""

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostListAPIView(generics.ListAPIView):
    """投稿投稿記事の取得（一覧）APIクラス"""

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['id', 'title', 'article', 'short_description','created_at', 'updated_at', 'n_goods']


class BlogPostRetrieveAPIView(generics.RetrieveAPIView):
    """投稿投稿記事の取得（詳細）APIクラス"""

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostUpdateAPIView(generics.UpdateAPIView):
    """投稿記事の更新、一部更新APIクラス"""

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDestroyAPIView(generics.DestroyAPIView):
    """投稿記事の削除APIクラス"""

    queryset = BlogPost.objects.all()
