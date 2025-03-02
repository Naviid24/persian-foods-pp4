from django.test import TestCase
from .forms import CommentForm, PostForm
from django.core.files.uploadedfile import SimpleUploadedFile
from blog.models import Category


class TestPostForm(TestCase):
    """
    Class-based testing approach to test
    our post form componnent by automatedt testing
    """

    def test_post_form_is_valid(self):
        # Creates a test category
        category = Category.objects.create(title="Meat")
        
        # Simulating an image upload
        fake_image = SimpleUploadedFile(
            "test.jpg",
            b"file_content",
            content_type="image/jpeg"
            )

        post_form = PostForm({
            'title': 'Koobideh',
            'content': 'Describe your post here',
            'featured_image': fake_image,
            'ingredients': 'herbs',
            'instructions': 'mixed spices',
            'status': 1, 
            'excerpt': 'Koobideh is one of the nice foods.',
            'slug': 'koobideh',
            'category': category.id,
        })

        # Checking if the form is valid
        self.assertTrue(
            post_form.is_valid(),
            msg='Post form is not valid'
            )


class TestCommentForm(TestCase):
    """
    Class-based testing approach to test
    our comment componnent by automatedt testing 
    """
    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This post is greate'})
        self.assertTrue(
            comment_form.is_valid(),
            msg='Comment form is not valid'
            )

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")

