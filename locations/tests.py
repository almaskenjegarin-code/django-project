from django.test import TestCase, Client
from django.urls import reverse
from .models import Location

class LocationsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.location = Location.objects.create(
            name='Test Eco Point',
            address='123 Green St',
            latitude=51.505,
            longitude=-0.09
        )

    def test_locations_map_loads(self):
        response = self.client.get(reverse('locations_home'))
        self.assertEqual(response.status_code, 200)
        
        # Verify context contains the locations queryset
        self.assertIn('locations', response.context)
        
        # Verify the template renders the location name
        self.assertContains(response, 'Test Eco Point')
