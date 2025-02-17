from django.db import models
from django.contrib.auth.models import User




STATUS = ((0, "Draft"), (1, "Published"))



#............... Category model...............
class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


#............... Post model...............
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)    
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.CharField(max_length=300, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()


#............... Comment model...............
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


#............... Like model...............
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker")

    class Meta:
        unique_together = ('post', 'user') # Prevents duplicate likes from the same user

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"
