from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from posts.forms import PostForm, CommentForm
from accounts.models import UserProfile
from posts.models import Post
from comments.models import Comment


def newcomment(request,pk):
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid:
            c=form.save(commit=False)
            c.c_author=request.user
            c.post=Post.objects.get(pk=pk)
            form.save()
            return redirect('postdetail',pk=pk)

    else:
        form=CommentForm()
    return render(request,'createcomment.html',{'form':form})

