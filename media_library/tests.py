from django.test import TestCase
from django.urls import reverse
from .models import Category, MediaItem

class MediaHubTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Learning", slug="learning")
        self.item = MediaItem.objects.create(
            title="Django Basics", media_type="video", category=self.category,
            file="library/demo.mp4", description="A sample learning video"
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MediaHub")

    def test_library_search(self):
        response = self.client.get(reverse("library"), {"q": "Django"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django Basics")

    def test_detail_page_loads(self):
        response = self.client.get(reverse("media_detail", args=[self.item.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django Basics")
