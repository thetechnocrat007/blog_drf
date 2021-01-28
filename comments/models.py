from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# Create your models here.
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    c_author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    
    parent=models.ForeignKey('Comment',null=True,blank=True,on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    created_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content[:50]