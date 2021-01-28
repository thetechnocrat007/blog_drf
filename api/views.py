from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializers import UserDetailSerializer,CommentSerializer,PostSerializer

from accounts.models import UserProfile
from django.contrib.auth.models import User

from posts.models import Post
from comments.models import Comment

# Create your views here.
class UserList(ModelViewSet):
    serializer_class=UserDetailSerializer
    queryset=User.objects.all()


class CommentList(ModelViewSet):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()
    lookup_field='post'
    """def get_queryset(self):
        pk=self.kwargs['pk']
        p=Post.objects.get(id=pk)
        return Comment.objects.filter(post=p)"""


class PostList(ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.objects.all()