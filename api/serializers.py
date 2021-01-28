from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import UserProfile
from posts.models import Post
from comments.models import Comment

User=get_user_model()

class UserDetailSerializer(ModelSerializer):
    email=serializers.EmailField(required=True)
    username=serializers.CharField(required=True)
    password=serializers.CharField(min_length=8,write_only=True)

    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
        extra_kwargs={'password':{'write_only':True}}




class PostSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=['id','title','content','likes','author','created_on']




class CommentSerializer(ModelSerializer):
    
    class Meta:
        model=Comment
        fields=['content','likes','c_author','created_on','parent','post']
