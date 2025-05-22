from django.test import TestCase
from .models import Artist

class ArtistModelTest(TestCase):
    def setUp(self):
        Artist.objects.create(name="Test Artist", bio="Bio of Test Artist", contact="test@example.com")

    def test_artist_str(self):
        artist = Artist.objects.get(name="Test Artist")
        self.assertEqual(str(artist), "Test Artist")