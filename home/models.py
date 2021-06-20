from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    desc = models.TextField()
    author = models.CharField(max_length=100, null=True, blank=True)
    poster = models.ImageField(upload_to="static/blog_img", null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
