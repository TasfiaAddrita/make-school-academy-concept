from django.test import TestCase
from django.contrib.auth.models import User
from tutorials.models import Tutorial

# Create your tests here.
class TutorialTestCase(TestCase):
    # canary test -- minimal tests that quickly verify that the system works as expected
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)
    
class TutorialListViewTests(TestCase):
    def test_multiple_pages(self):
        # Make some test data to be displayed on page
        user = User.objects.create()
        Tutorial.objects.create(title="My Test Tutorial", description="test")
        Tutorial.objects.create(title="Another Test Tutorial", description="test")
        
        # Issue a GET request to the MakeWiki homepage
        # When we make a request, we should get a response back
        response = self.client.get('/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template matches
        # the number of pages we have in the database
        responses = response.context['tutorials']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Tutorial: My Test Tutorial>', '<Tutorial: Another Test Tutorial>'],
            ordered=False
        )