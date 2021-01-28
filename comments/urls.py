from . import views
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('comment/<int:pk>',views.newcomment, name='newcomment'),
]