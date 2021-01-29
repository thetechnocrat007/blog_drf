from django.forms import ModelForm
from django import forms
from posts.models import Post
from comments.models import Comment
class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','content']


class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['content']


