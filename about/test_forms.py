from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):
    """
    Automated tests for the PostForm.

    This class tests the validation of the PostForm, ensuring:
    - The form is valid when all required fields are provided.
    - The form correctly identifies missing or incorrect fields.
    """

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )
