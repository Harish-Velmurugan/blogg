from django.db import models
from datetime import datetime 
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    def __str__ (self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    
    comment = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    def __str__ (self):
        return self.comment
    def get_absolute_url(self):
        return reverse("home")
