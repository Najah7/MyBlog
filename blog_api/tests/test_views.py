import uuid

from django.contrib.auth import get_user_model
from django.utils.timezone import localtime
from rest_framework.test import APITestCase

from ..models import BlogPost

class TestPostCreateAPIView(APITestCase):

    TARGET_URL = '/api/blog/create/'

    def test_create_success(self):
        """投稿記事の登録APIへのPOSTリクエスト（正常系）"""

        params = {
            "id": uuid.uuid4(),
            "title": "test",
            "article": "test",
            "short_description": "test",
            "created_at": "2023-01-06T23:02:31.064472+09:00",
            "updated_at": "2023-01-06T23:02:29+09:00",
            "n_goods": 0
        }

        self.client.force_login()
        response = self.client.post(self.TARGET_URL, params, format='json')

        self.assertEqual(response.status_code, 201)

        post = BlogPost.objects.get()
        expected_json_dict = {
            'id': str(post.id),
            'title': post.title,
            "article": post.article,
            "short_description": post.short_description,
            "created_at": str(post.created_at),
            "updated_at": str(post.updated_at),
            "n_goods": str(post.n_goods)
        }

        self.assertJSONEqual(response.content, expected_json_dict)

