from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
 
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_user = models.CharField(max_length=200, null=True)
    comment_date = models.DateTimeField(auto_now_add=True, null=True)
    comment_textfield = models.TextField()