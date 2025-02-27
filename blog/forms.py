from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    """
    Post Form to create/add new post
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'featured_image',
            'ingredients',
            'instructions',
            'status',
            'excerpt',
            'slug',
        ]

        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
            'content': forms.Textarea(
                attrs={'rows': 5, 'placeholder': 'Describe your recipe here'}),
        }

        labels = {
            'title': 'Recipe Title',
            'content': 'Description',
            'featured_image': 'Recipe Image',
            'ingredients': 'Recipe Ingredients',
            'instructions': 'Recipe Instructions',
            'status': 'Status (Save as a Draft / Publish Now)',
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)