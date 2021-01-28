from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import UserList
from api.views import PostList
from api.views import CommentList

router=DefaultRouter()
router.register('user',UserList,basename='user')
router.register('comment',CommentList,basename='comment')
router.register('post',PostList,basename='post')

urlpatterns=router.urls

