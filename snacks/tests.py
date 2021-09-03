from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

# Create your tests here.
class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='laithhussein',
            email='laithalsanory9919@gmail.com',
            password='123123123'
        )
        self.snack = Snack.objects.create(
            title='potato',
            purshaser=self.user,
            description='potato with cheese'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "potato")

    def test_thing_content(self):
        self.assertEqual(self.snack.title, 'potato')
        self.assertEqual(str(self.snack.purshaser), 'laith')
        self.assertEqual(self.snack.description, 'potato with cheese ')

    def test_snack_list_view(self):
        expected = 200
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, expected)
        self.assertContains(response, "potato")
        self.assertTemplateUsed(response, "snack_list.html")


    def test_snack_details_view(self):
        expected = 200
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/800/")
        self.assertEqual(response.status_code, expected)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "potato")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        expected = 200
        actual = self.client.post(reverse('create_snack'),{'title': 'burger', ' purshaser': self.user,'description': 'potato with cheese',})
        self.assertEqual(expected, actual.status_code)
        self.assertContains(actual, 'potato with cheese')
        self.assertContains(actual, 'laith')

    def test_snack_update_view(self):
        expected = 200
        actual = self.client.post(reverse('update_snack', args='1')).status_code
        self.assertEqual(expected, actual)

    def test_snack_delete_view(self):
        expected = 200
        actual = self.client.get(reverse('delete_snack', args='1')).status_code
        self.assertEqual(expected, actual)