from . import views
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('createpost',views.newpost, name='createpost'),
    path('posts',views.PostList.as_view(), name='allposts'),
    path('postsbyauthor/<int:pk>',views.PostListbyAuthor.as_view(), name='postsbyauthor'),
    path('post/<int:pk>',views.PostDetail.as_view(), name='postdetail'),
]