from django.db import models
from django.template.defaultfilters import slugify, title 
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=255, null= False)
    image = models.ImageField(upload_to='site_media')
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    #vote counter
    votes_total = models.ManyToManyField(User, related_name="votes")
    
    def get_absolute_url(self):
        return reverse("model_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
            super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "posts"
        ordering = ['created_on']

        def __unicode__(self):
            return self.title

class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

