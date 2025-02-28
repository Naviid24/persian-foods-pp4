from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """Category model for organizing posts."""

    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    """Post model representing blog posts."""

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    content = models.TextField()
    ingredients = models.TextField(blank=False, default="ingredients")
    instructions = models.TextField(blank=False, default="ingredients")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.CharField(max_length=300, blank=True)
    featured_image = CloudinaryField("image", default="placeholder")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def total_likes(self):
        """Returns the total number of likes for the post."""
        return self.likes.count()
    
    def save(self, *args, **kwargs):
        """
        A method to generate slug for posts submitted 
        by user through the site form
        """
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    """Comment model for user comments on posts."""

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


class Like(models.Model):
    """Like model for tracking likes on posts."""

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="likes"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="liker"
    )

    class Meta:
        unique_together = ("post", "user")  # Prevents duplicate likes

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"
