from . import views
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('signup',views.signup,name='signup'),
    path('',views.home,name='home'),
    path('login',LoginView.as_view(), name='login'),
    path('logout',LogoutView.as_view(), name='logout'),
]