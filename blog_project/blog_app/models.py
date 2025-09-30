from django.db import models

class BlogPost(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200)
    content = models.TextField(verbose_name="Content")
    author = models.CharField(verbose_name="Author",max_length=100)
    created_at = models.DateTimeField(verbose_name="created date",auto_now_add=True)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title
