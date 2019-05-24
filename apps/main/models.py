from django.db import models

# Create your models here.
class User(models.Model):
    # properties => columns
    # id (django does this)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    # created_at, updated_at
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # created_posts
    # all posts: user.created_posts.all() [Post,Post,Post]

    # liked_posts

    def __str__(self):
        return self.username

class Post(models.Model):

    content = models.TextField()
    topic = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # User
    author = models.ForeignKey(User, related_name="created_posts")

    # [User,User]
    likes = models.ManyToManyField(User, related_name="liked_posts")