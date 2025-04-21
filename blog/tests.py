from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post
# Create your tests here.


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",email="test@email.com",password="secret"
        )
        cls.post= Post.objects.create(
            title = "A great title",
            body = "Nice Body Content",
            author = cls.user,
        )
    def test_post_model(self):
        self.assertEqual(self.post.title,"A great title")
        self.assertEqual(self.post.body,"Nice Body Content")
        self.assertEqual(self.post.author.username,"testuser")
        self.assertEqual(str(self.post),"A great title")
        self.assertEqual(self.post.get_absolute_url(),'/post/1/')