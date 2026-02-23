from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

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
    def test_url_exists_at_correct_location_listview(self):  # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):  # new
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):  # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice Body Content")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detailview(self):  # new
        response = self.client.get(reverse("post_detail", 
          kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A great title")
        self.assertTemplateUsed(response, "post_detail.html")
    
    def test_post_createview(self):
        self.client.login(username="testuser", password="secret")
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "New title",
                "body": "New text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.first().title, "New title")
        self.assertEqual(Post.objects.first().body, "New text")

    def test_post_updateview(self):
        self.client.login(username="testuser", password="secret")
        response = self.client.post(
            reverse("post_edit", args="1"),
            {
                "title": "Updated title",
                "body": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.first().title, "Updated title")
        self.assertEqual(Post.objects.first().body, "Updated text")

    def test_post_deleteview(self):
        self.client.login(username="testuser", password="secret")
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)