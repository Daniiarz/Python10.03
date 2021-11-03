from django.db import models


class BlogPost(models.Model):
    image = models.FileField(upload_to="blog_pics/", null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:15]


class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=100)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post} - {self.text}"
