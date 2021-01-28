from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    content=models.TextField()
    likes=models.IntegerField(default=0)
    created_on=models.DateField(default=date.today)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('postdetail', args=[str(self.pk)])