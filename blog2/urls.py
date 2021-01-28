from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[

    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('',include('posts.urls')),
    path('',include('comments.urls')),
    path('api/',include('api.urls')),

]