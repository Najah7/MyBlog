import uuid

from django.test import TestCase
# from django.utils.timezone import localtime

# from ..models import BlogPost
from ..serializers import BlogPostSerializer

class TestBlogPostSerializer(TestCase):
    """BlogPostSerializerのテスト"""

    def test_input_vaild(self):
        """入力データのバリデーション（OK）"""

        true_input_data = {
            "id": uuid.uuid4(),
            "title": "test",
            "article": "test",
            # イメージフィールドのところだけシリアライザをどうテストするのかわからず、なので一度放置する。
            # "thumbnail": "http://127.0.0.1:8000/media/images/NYC_times_square.png",
            "short_description": "test",
            "created_at": "2023-01-06T23:02:31.064472+09:00",
            "updated_at": "2023-01-06T23:02:29+09:00",
            "n_goods": 0
        }

        false_input_data = {
            "title": "test",
        }

        serializer = BlogPostSerializer(data=true_input_data)

        self.assertTrue(serializer.is_valid())


        # TODO:しっかり分けて
        serializer = BlogPostSerializer(data=false_input_data)

        self.assertFalse(serializer.is_valid())

