
from django.db import models

# Create your models here.

class BlogPost(models.Model):
    author_name = models.CharField(max_length=100)
    upload_time = models.DateTimeField(auto_now_add=True)
    post_text = models.TextField()
    post_title = models.CharField(max_length=100,unique=True)


    def __str__(self) -> str:
        return self.post_title





