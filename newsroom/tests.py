from django.test import TestCase
from . models import ParentInfograph
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the ParentInfograph model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.parentinfograph_name = "Write world class code"
        self.parentinfograph = ParentInfograph(name=self.parentinfograph_name)

    def test_model_can_create_a_parentinfograph(self):
        """Test the parentinfograph model can create a parentinfograph."""
        old_count = ParentInfograph.objects.count()
        self.parentinfograph.save()
        new_count = ParentInfograph.objects.count()
        self.assertNotEqual(old_count, new_count)



# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.parentinfograph_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.parentinfograph_data,
            format="json")

    def test_api_can_create_a_parentinfograph(self):
        """Test the api has parentinfograph creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_api_can_get_a_parentinfograph(self):
        """Test the api can get a given parentinfograph."""
        parentinfograph = ParentInfograph.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': parentinfograph.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, parentinfograph)

    def test_api_can_update_parentinfograph(self):
        """Test the api can update a given parentinfograph."""
        change_parentinfograph = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': parentinfograph.id}),
            change_parentinfograph, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_parentinfograph(self):
        """Test the api can delete a parentinfograph."""
        parentinfograph = ParentInfograph.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': parentinfograph.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
