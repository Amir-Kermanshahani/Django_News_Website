from email.policy import default
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):

    title = models.CharField(max_length = 200) 
    
    def __str__(self):
        return self.title
    



class Post(models.Model):

    title = models.CharField(max_length=255, blank=True, default='')
    category = models.ManyToManyField(Category)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated_at = models.DateTimeField(auto_now = True, blank = True)
    body = models.TextField(blank=True, default='')
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE, blank = True, null = True)
    source = models.CharField(max_length=255, default = str(author))
    featured_image = models.ImageField(upload_to='uploads/post_images/', blank = True, null=True)
    views_number = models.PositiveIntegerField(null = True)
    comments_number = models.PositiveIntegerField(null = True)
    released = models.BooleanField(default = False, blank = True)
    featured = models.BooleanField(default = False, blank = True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    


class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    subject = models.CharField(max_length = 255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name