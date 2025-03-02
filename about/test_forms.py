from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):
    """
    Automated tests for the PostForm.

    This class tests the validation of the PostForm, ensuring:
    - The form is valid when all required fields are provided.
    - The form correctly identifies missing or incorrect fields.
    """

    def test_form_is_valid(self):
        """ Test for all fields"""
    
        form = CollaborateForm({
            'name': 'David',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="About form is not valid")