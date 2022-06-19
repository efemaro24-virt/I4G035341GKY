from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.Title