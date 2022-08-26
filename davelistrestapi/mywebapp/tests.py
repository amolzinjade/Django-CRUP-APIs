from django.test import TestCase
from mywebapp.models import listing
from mywebapp.models import Image
from mywebapp.models import Message
from django.urls import reverse
from django.contrib.auth import get_user_model

class ListingTestCase(TestCase):    
        def create_listing(self, title="BMW", content="This is good car",categories="PRIVATE"):
            return listing.objects.create(title=title, content=content, categories=categories)

        def test_listing_creation(self):
            w = self.create_listing()
            self.assertTrue(isinstance(w, listing))
            self.assertEqual(w.__str__(), w.title)

class ImageTestCase(TestCase):    
        def create_image(self, property_id=1):
            return Image.objects.create(property_id=property_id)

        def test_image_creation(self):
            i = self.create_image()
            self.assertTrue(isinstance(i, Image))
            self.assertEqual(i.__int__(), i.property_id)

class ViewListingTestCase(TestCase):    
    def test_list_view(self):
        url = reverse("CreateListing")
        print("URL="+url)
        resp = self.client.get("127.0.0.1"+url)
        self.assertEqual(resp.status_code, 200)
        