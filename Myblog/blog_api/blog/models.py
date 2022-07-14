from django.db import models

# Create your models here.

class Blog(models.Model):
    author = models.CharField(max_length=30, null=True,blank=False)
    title = models.CharField(max_length=100, null=True,blank=False)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title